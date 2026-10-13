#!/usr/bin/env python3
"""Cắt short 9:16 từ video dài: Claude chọn đoạn hay từ phụ đề SRT, ffmpeg cắt + cháy phụ đề.

Ví dụ:
    python tools/cat_short.py final_16x9.mp4 subtitles.srt --out 8_shorts
    python tools/cat_short.py final_16x9.mp4 subtitles.srt --out 8_shorts --mode blur
    python tools/cat_short.py final_16x9.mp4 subtitles.srt --out 9_shorts --mode blur --note "Not financial advice · Capital at risk"
    python tools/cat_short.py final_16x9.mp4 subtitles.srt --out 8_shorts --plan-only   # chỉ để Claude chọn đoạn
    python tools/cat_short.py final_16x9.mp4 subtitles.srt --out 8_shorts --plan 8_shorts/plan.json  # cắt theo plan có sẵn

Đầu ra trong thư mục --out: short_01.mp4 … , plan.json (đoạn Claude chọn, sửa tay được), shorts.csv (tiêu đề/caption).
Cần: ffmpeg + ffprobe trong PATH; biến môi trường ANTHROPIC_API_KEY (trừ khi dùng --plan).
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

DEFAULT_MODEL = "claude-opus-5-5"
OUT_W, OUT_H = 1080, 1920
# Lề đầu/cuối mỗi short để không cắt mất âm tiết.
PAD_START, PAD_END = 0.15, 0.35
# Không bắt đầu short bằng các từ nối trỏ về đoạn trước.
WEAK_OPENERS = ("and ", "so ", "but ", "this ", "that ", "it ", "they ", "he ", "she ", "as we ", "meanwhile")


@dataclass
class Cue:
    num: int  # số thứ tự 1-based trong file SRT (sau khi đánh lại)
    start: float
    end: float
    text: str


# ----------------------------------------------------------------- SRT

_TS = re.compile(r"(\d+):(\d{2}):(\d{2})[,.](\d{1,3})")


def _ts_to_sec(ts: str) -> float:
    m = _TS.search(ts)
    if not m:
        raise ValueError(f"Mốc thời gian SRT không hợp lệ: {ts!r}")
    h, mi, s, ms = m.groups()
    return int(h) * 3600 + int(mi) * 60 + int(s) + int(ms.ljust(3, "0")) / 1000


def parse_srt(path: Path) -> list[Cue]:
    raw = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    cues: list[Cue] = []
    for block in re.split(r"\n\s*\n", raw.strip()):
        lines = [ln.strip() for ln in block.split("\n") if ln.strip()]
        arrow = next((i for i, ln in enumerate(lines) if "-->" in ln), None)
        if arrow is None:
            continue
        left, right = lines[arrow].split("-->", 1)
        text = " ".join(re.sub(r"<[^>]+>", "", ln) for ln in lines[arrow + 1:]).strip()
        if not text:
            continue
        cues.append(Cue(len(cues) + 1, _ts_to_sec(left), _ts_to_sec(right), text))
    if not cues:
        raise ValueError(f"Không đọc được dòng phụ đề nào trong {path}")
    return cues


def fmt_ts(sec: float) -> str:
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


# ----------------------------------------------------------------- Claude

CLIP_SCHEMA = {
    "type": "object",
    "properties": {
        "clips": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "first_cue": {"type": "integer"},
                    "last_cue": {"type": "integer"},
                    "title": {"type": "string"},
                    "reason": {"type": "string"},
                    "youtube_title": {"type": "string"},
                    "tiktok_caption": {"type": "string"},
                    "instagram_caption": {"type": "string"},
                    "facebook_caption": {"type": "string"},
                    "hashtags": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["first_cue", "last_cue", "title", "reason", "youtube_title",
                             "tiktok_caption", "instagram_caption", "facebook_caption", "hashtags"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["clips"],
    "additionalProperties": False,
}

SYSTEM_PROMPT = """You are the Shorts editor of an English-language YouTube review channel (software, AI tools, tech products, trading platforms; global audience).
You receive the numbered subtitle cues of a finished long-form review. Pick segments that work as standalone vertical Shorts.

Rules for every segment:
- It is a run of consecutive cues from first_cue to last_cue (inclusive) and lasts between {min_s} and {max_s} seconds; aim for 30-50 seconds.
- The first cue must make sense on its own: never start on a cue that opens with a connector or a pronoun pointing back ("And", "So", "But", "This", "That", "It", "They", "As we saw", "Meanwhile").
- The first sentence should create curiosity; the last cue should land a payoff, twist or surprising fact.
- Prefer self-contained parts: one feature demo, the pricing breakdown, a head-to-head comparison, the verdict. Skip the disclosure, the channel outro and calls to action.
- Only use claims that are in the transcript. Never pick a segment that promises profits, gives investment advice or presents a personal testimonial.
- Segments must not overlap. Order them from strongest to weakest.

Text fields (English, no emojis in titles):
- title: 3-6 word internal name.
- reason: one sentence on why it works as a Short.
- youtube_title: at most 60 characters, keyword early.
- tiktok_caption: at most 150 characters, no hashtags inside; end with "(affiliate link in description)" when a product with a link is named.
- instagram_caption: at most 2 sentences.
- facebook_caption: at most 2 sentences.
- Never use the words guaranteed, risk-free, profit, get rich in any field.
- hashtags: 3-5 items, each starting with '#', no spaces."""


def build_transcript(cues: list[Cue]) -> str:
    return "\n".join(f"#{c.num} [{fmt_ts(c.start)} -> {fmt_ts(c.end)}] {c.text}" for c in cues)


def ask_claude(cues: list[Cue], count: int, min_s: float, max_s: float, model: str, client=None) -> dict:
    """Gọi Claude để chọn đoạn. Trả về dict theo CLIP_SCHEMA."""
    import anthropic

    client = client or anthropic.Anthropic()
    request = dict(
        model=model,
        max_tokens=16000,
        system=SYSTEM_PROMPT.format(min_s=int(min_s), max_s=int(max_s)),
        output_config={"effort": "medium", "format": {"type": "json_schema", "schema": CLIP_SCHEMA}},
        messages=[{
            "role": "user",
            "content": f"Pick the {count} best Shorts from this video.\n\nSubtitle cues:\n{build_transcript(cues)}",
        }],
    )
    try:
        # fallbacks="default": nếu bộ lọc an toàn từ chối nhầm, API tự chạy lại trên model dự phòng.
        response = client.beta.messages.create(
            **request, betas=["server-side-fallback-2026-07-01"], fallbacks="default")
    except anthropic.BadRequestError as err:
        if "fallback" not in str(err).lower():
            raise
        response = client.messages.create(**request)

    if response.stop_reason == "refusal":
        raise RuntimeError("Claude từ chối yêu cầu này (stop_reason=refusal). Kiểm tra nội dung phụ đề.")
    if response.stop_reason == "max_tokens":
        raise RuntimeError("Phản hồi bị cắt do max_tokens. Giảm --count hoặc chia nhỏ video.")
    text = next((b.text for b in response.content if b.type == "text"), None)
    if text is None:
        raise RuntimeError("Phản hồi của Claude không có nội dung văn bản.")
    return json.loads(text)


# ----------------------------------------------------------------- Plan validation

def _duration(cues: list[Cue], first: int, last: int) -> float:
    return cues[last - 1].end - cues[first - 1].start


def normalize_plan(plan: dict, cues: list[Cue], count: int, min_s: float, max_s: float) -> tuple[list[dict], list[str]]:
    """Kiểm tra & chỉnh đoạn Claude (hoặc người) chọn cho hợp lệ. Trả về (clips, cảnh báo)."""
    n = len(cues)
    warnings: list[str] = []
    accepted: list[dict] = []
    used: list[tuple[int, int]] = []
    for i, clip in enumerate(plan.get("clips", []), start=1):
        first = int(clip.get("first_cue", 0))
        last = int(clip.get("last_cue", 0))
        if not (1 <= first <= n and 1 <= last <= n):
            warnings.append(f"Bỏ đoạn {i}: cue {first}-{last} nằm ngoài 1-{n}.")
            continue
        if last < first:
            first, last = last, first
        while _duration(cues, first, last) > max_s and last > first:
            last -= 1
        while _duration(cues, first, last) < min_s and last < n:
            last += 1
        dur = _duration(cues, first, last)
        if not (min_s <= dur <= max_s):
            warnings.append(f"Bỏ đoạn {i}: không chỉnh được về {min_s:.0f}-{max_s:.0f} giây (hiện {dur:.1f} giây).")
            continue
        if any(not (last < a or first > b) for a, b in used):
            warnings.append(f"Bỏ đoạn {i}: trùng với đoạn đã chọn (cue {first}-{last}).")
            continue
        if cues[first - 1].text.lower().startswith(WEAK_OPENERS):
            warnings.append(f"Đoạn {i} mở bằng từ nối: “{cues[first - 1].text[:40]}…” — nên xem lại.")
        used.append((first, last))
        accepted.append({**clip, "first_cue": first, "last_cue": last})
        if len(accepted) == count:
            break
    if len(accepted) < count:
        warnings.append(f"Chỉ có {len(accepted)}/{count} đoạn hợp lệ.")
    return accepted, warnings


# ----------------------------------------------------------------- Subtitles for Shorts

ASS_HEADER = """[Script Info]
ScriptType: v4.00+
PlayResX: {w}
PlayResY: {h}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Short,{font},{size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,0,2,80,160,{margin_v},1
Style: Note,{font},44,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,3,10,0,8,80,160,{note_margin_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def _ass_ts(sec: float) -> str:
    cs = int(round(max(sec, 0) * 100))
    h, cs = divmod(cs, 360_000)
    m, cs = divmod(cs, 6000)
    s, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def chunk_cue(cue: Cue, words_per_chunk: int) -> list[tuple[float, float, str]]:
    """Chia 1 dòng phụ đề thành cụm 1-N từ, chia thời gian theo số ký tự (kiểu phụ đề short)."""
    words = cue.text.split()
    chunks = [" ".join(words[i:i + words_per_chunk]) for i in range(0, len(words), words_per_chunk)]
    total = sum(len(c) for c in chunks) or 1
    out, t = [], cue.start
    for c in chunks:
        d = (cue.end - cue.start) * len(c) / total
        out.append((t, t + d, c))
        t += d
    return out


def _ass_text(text: str) -> str:
    return text.replace("\\", "\\\\").replace("{", "(").replace("}", ")")


def write_ass(path: Path, cues: list[Cue], clip_start: float, clip_end: float,
              font: str, size: int, words_per_chunk: int, note: str | None = None,
              burn_subs: bool = True) -> None:
    """Viết file phụ đề ASS cho 1 short. `note` = dòng cố định suốt short (ví dụ cảnh báo rủi ro)."""
    lines = [ASS_HEADER.format(w=OUT_W, h=OUT_H, font=font, size=size, margin_v=int(OUT_H * 0.27),
                               note_margin_v=int(OUT_H * 0.16))]
    if note:
        lines.append(f"Dialogue: 1,{_ass_ts(0)},{_ass_ts(clip_end - clip_start)},Note,,0,0,0,,{_ass_text(note)}")
    if not burn_subs:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return
    for cue in cues:
        if cue.end <= clip_start or cue.start >= clip_end:
            continue
        for s, e, text in chunk_cue(cue, words_per_chunk):
            s, e = max(s, clip_start) - clip_start, min(e, clip_end) - clip_start
            if e - s < 0.05:
                continue
            lines.append(f"Dialogue: 0,{_ass_ts(s)},{_ass_ts(e)},Short,,0,0,0,,{_ass_text(text)}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ----------------------------------------------------------------- ffmpeg

def probe_duration(video: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(video)],
        check=True, capture_output=True, text=True).stdout.strip()
    return float(out)


def video_filter(mode: str, ass_name: str | None) -> str:
    if mode == "crop":
        chain = f"[0:v]scale={OUT_W}:{OUT_H}:force_original_aspect_ratio=increase,crop={OUT_W}:{OUT_H},setsar=1"
    else:  # blur: video gốc ở giữa, nền là chính video phóng to + làm mờ
        chain = (f"[0:v]split[a][b];"
                 f"[a]scale={OUT_W}:{OUT_H}:force_original_aspect_ratio=increase,crop={OUT_W}:{OUT_H},boxblur=20:2[bg];"
                 f"[b]scale={OUT_W}:{OUT_H}:force_original_aspect_ratio=decrease[fg];"
                 f"[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1")
    chain += ",fps=30"
    if ass_name:
        chain += f",ass={ass_name}"
    return chain + "[v]"


def render_clip(video: Path, out_dir: Path, name: str, start: float, end: float, mode: str,
                ass_name: str | None, loudnorm: bool) -> None:
    cmd = ["ffmpeg", "-y", "-v", "error", "-ss", f"{start:.3f}", "-i", str(video.resolve()), "-t", f"{end - start:.3f}",
           "-filter_complex", video_filter(mode, ass_name), "-map", "[v]", "-map", "0:a?",
           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart"]
    if loudnorm:
        cmd += ["-af", "loudnorm=I=-14:TP=-1:LRA=11"]
    cmd.append(name)
    # Chạy trong thư mục đầu ra để đường dẫn file .ass không cần thoát ký tự (Windows: C:\...).
    subprocess.run(cmd, check=True, cwd=out_dir)


# ----------------------------------------------------------------- main

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Cắt short 9:16 từ video dài bằng Claude + ffmpeg.")
    p.add_argument("video", type=Path, help="Video dài đã dựng xong (MP4)")
    p.add_argument("srt", type=Path, help="Phụ đề SRT của video đó")
    p.add_argument("--out", type=Path, default=Path("shorts"), help="Thư mục đầu ra (mặc định: shorts)")
    p.add_argument("--count", type=int, default=5, help="Số short cần cắt (mặc định 5)")
    p.add_argument("--min", dest="min_s", type=float, default=20, help="Độ dài tối thiểu (giây)")
    p.add_argument("--max", dest="max_s", type=float, default=90, help="Độ dài tối đa (giây)")
    p.add_argument("--mode", choices=["crop", "blur"], default="crop",
                   help="crop = cắt giữa khung (cần bố cục chủ thể ở giữa); blur = video ở giữa, nền mờ")
    p.add_argument("--plan", type=Path, help="Dùng plan.json có sẵn thay vì hỏi Claude")
    p.add_argument("--plan-only", action="store_true", help="Chỉ để Claude chọn đoạn, không cắt video")
    p.add_argument("--model", default=DEFAULT_MODEL, help=f"Model Claude (mặc định {DEFAULT_MODEL})")
    p.add_argument("--no-subs", action="store_true", help="Không cháy phụ đề vào short")
    p.add_argument("--note", help='Dòng chữ cố định phía trên suốt short, ví dụ "Not financial advice · Capital at risk"')
    p.add_argument("--font", default="Arial", help="Font phụ đề (mặc định Arial)")
    p.add_argument("--font-size", type=int, default=78, help="Cỡ chữ phụ đề, pixel trên khung 1080x1920")
    p.add_argument("--words", type=int, default=4, help="Số từ tối đa mỗi lần hiện phụ đề (mặc định 4)")
    p.add_argument("--no-loudnorm", action="store_true", help="Không chuẩn hoá âm lượng -14 LUFS")
    a = p.parse_args(argv)

    for tool in ("ffmpeg", "ffprobe"):
        if not a.plan_only and shutil.which(tool) is None:
            p.error(f"Không tìm thấy {tool}. Cài ffmpeg và thêm vào PATH.")
    if not a.video.exists() or not a.srt.exists():
        p.error("Không tìm thấy file video hoặc SRT.")
    if a.min_s >= a.max_s:
        p.error("--min phải nhỏ hơn --max")

    cues = parse_srt(a.srt)
    a.out.mkdir(parents=True, exist_ok=True)
    print(f"Đọc {len(cues)} dòng phụ đề ({fmt_ts(cues[-1].end)}).")

    if a.plan:
        plan = json.loads(a.plan.read_text(encoding="utf-8"))
    else:
        print(f"Đang nhờ Claude ({a.model}) chọn {a.count} đoạn…")
        plan = ask_claude(cues, a.count, a.min_s, a.max_s, a.model)

    clips, warnings = normalize_plan(plan, cues, a.count, a.min_s, a.max_s)
    for w in warnings:
        print("⚠", w)
    if not clips:
        print("Không có đoạn hợp lệ nào. Dừng.", file=sys.stderr)
        return 1
    plan_path = a.out / "plan.json"
    plan_path.write_text(json.dumps({"clips": clips}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã lưu {plan_path} (sửa tay được, chạy lại với --plan).")

    video_len = None if a.plan_only else probe_duration(a.video)
    rows = []
    for i, clip in enumerate(clips, start=1):
        first, last = cues[clip["first_cue"] - 1], cues[clip["last_cue"] - 1]
        start = max(0.0, first.start - PAD_START)
        end = last.end + PAD_END if video_len is None else min(video_len, last.end + PAD_END)
        name = f"short_{i:02d}.mp4"
        if not a.plan_only:
            ass_name = None
            if not a.no_subs or a.note:
                ass_name = f"short_{i:02d}.ass"
                write_ass(a.out / ass_name, cues, start, end, a.font, a.font_size, max(1, a.words),
                          note=a.note, burn_subs=not a.no_subs)
            print(f"[{i}/{len(clips)}] {name}: {fmt_ts(start)} → {fmt_ts(end)} ({end - start:.1f} giây) — {clip['title']}")
            render_clip(a.video, a.out, name, start, end, a.mode, ass_name, not a.no_loudnorm)
        rows.append({
            "file": name, "start": fmt_ts(start), "end": fmt_ts(end), "duration_s": round(end - start, 1),
            "title": clip["title"], "youtube_title": clip["youtube_title"],
            "tiktok_caption": clip["tiktok_caption"], "instagram_caption": clip["instagram_caption"],
            "facebook_caption": clip["facebook_caption"], "hashtags": " ".join(clip["hashtags"]),
            "first_line": first.text, "last_line": last.text, "reason": clip["reason"],
        })

    csv_path = a.out / "shorts.csv"
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:  # utf-8-sig để Excel đọc đúng
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Xong. {csv_path} có tiêu đề & caption cho {len(rows)} short.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
