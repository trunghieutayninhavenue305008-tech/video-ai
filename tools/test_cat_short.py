"""Kiểm thử cho cat_short.py — chạy: python -m unittest tools/test_cat_short.py -v"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cat_short as cs  # noqa: E402

SRT = """﻿1
00:00:00,000 --> 00:00:04,000
In 1992, a team of explorers found a city buried in the sand.

2
00:00:04,000 --> 00:00:09,500
Its name was Ubar, and legends said God himself destroyed it.

3
00:00:09,500 --> 00:00:15,000
And the satellites saw what the camels never could.

4
00:00:15,000 --> 00:00:22,000
Ancient caravan roads, invisible from the ground, all pointed to one place.

5
00:00:22,000 --> 00:00:30,000
But when they dug, the city was not destroyed by fire or war.

6
00:00:30,000 --> 00:00:38,000
It had collapsed into a sinkhole beneath its own well.

7
00:00:38,000 --> 00:00:45,000
Rome, by contrast, was never truly lost.
"""


def write_srt(tmp: Path) -> Path:
    p = tmp / "sub.srt"
    p.write_text(SRT.replace("\n", "\r\n"), encoding="utf-8")
    return p


def clip(first, last, title="t"):
    return {"first_cue": first, "last_cue": last, "title": title, "reason": "r", "youtube_title": "y",
            "tiktok_caption": "tt", "instagram_caption": "ig", "facebook_caption": "fb", "hashtags": ["#a", "#b"]}


class ParseTests(unittest.TestCase):
    def test_parse_srt_bom_crlf(self):
        with tempfile.TemporaryDirectory() as d:
            cues = cs.parse_srt(write_srt(Path(d)))
        self.assertEqual(len(cues), 7)
        self.assertEqual(cues[0].num, 1)
        self.assertAlmostEqual(cues[1].end, 9.5)
        self.assertTrue(cues[0].text.startswith("In 1992"))

    def test_fmt_ts(self):
        self.assertEqual(cs.fmt_ts(3723.4567), "01:02:03.457")


class PlanTests(unittest.TestCase):
    def setUp(self):
        with tempfile.TemporaryDirectory() as d:
            self.cues = cs.parse_srt(write_srt(Path(d)))

    def test_valid_and_overlap_and_range(self):
        plan = {"clips": [clip(1, 4), clip(3, 5), clip(5, 7), clip(9, 12)]}
        clips, warns = cs.normalize_plan(plan, self.cues, count=5, min_s=20, max_s=90)
        self.assertEqual([(c["first_cue"], c["last_cue"]) for c in clips], [(1, 4), (5, 7)])
        self.assertTrue(any("trùng" in w for w in warns))
        self.assertTrue(any("ngoài" in w for w in warns))

    def test_extend_short_and_trim_long(self):
        clips, _ = cs.normalize_plan({"clips": [clip(1, 1)]}, self.cues, 1, min_s=20, max_s=90)
        self.assertEqual((clips[0]["first_cue"], clips[0]["last_cue"]), (1, 4))  # 0→22 s
        clips, _ = cs.normalize_plan({"clips": [clip(1, 7)]}, self.cues, 1, min_s=10, max_s=30)
        self.assertEqual(clips[0]["last_cue"], 5)  # 0→30 s

    def test_weak_opener_warning(self):
        _, warns = cs.normalize_plan({"clips": [clip(3, 6)]}, self.cues, 1, min_s=20, max_s=90)
        self.assertTrue(any("từ nối" in w for w in warns))

    def test_count_limit(self):
        clips, _ = cs.normalize_plan({"clips": [clip(1, 4), clip(5, 7)]}, self.cues, 1, 20, 90)
        self.assertEqual(len(clips), 1)


class SubtitleTests(unittest.TestCase):
    def test_chunk_cue_timing(self):
        cue = cs.Cue(1, 10.0, 14.0, "one two three four five six seven")
        chunks = cs.chunk_cue(cue, 3)
        self.assertEqual([c[2] for c in chunks], ["one two three", "four five six", "seven"])
        self.assertAlmostEqual(chunks[0][0], 10.0)
        self.assertAlmostEqual(chunks[-1][1], 14.0)

    def test_write_ass_shifts_and_clips(self):
        with tempfile.TemporaryDirectory() as d:
            cues = cs.parse_srt(write_srt(Path(d)))
            path = Path(d) / "x.ass"
            cs.write_ass(path, cues, 15.0, 30.0, "Arial", 78, 4)
            text = path.read_text(encoding="utf-8")
        self.assertIn("PlayResX: 1080", text)
        dialogues = [ln for ln in text.splitlines() if ln.startswith("Dialogue:")]
        self.assertTrue(dialogues[0].startswith("Dialogue: 0,0:00:00.00,"))
        self.assertTrue(all("God himself" not in ln for ln in dialogues))  # cue 2 nằm ngoài đoạn


    def test_write_ass_note_only(self):
        with tempfile.TemporaryDirectory() as d:
            cues = cs.parse_srt(write_srt(Path(d)))
            path = Path(d) / "n.ass"
            cs.write_ass(path, cues, 15.0, 30.0, "Arial", 78, 4,
                         note="Not financial advice · Capital at risk", burn_subs=False)
            text = path.read_text(encoding="utf-8")
        dialogues = [ln for ln in text.splitlines() if ln.startswith("Dialogue:")]
        self.assertEqual(len(dialogues), 1)
        self.assertIn(",Note,", dialogues[0])
        self.assertIn("0:00:15.00", dialogues[0])
        self.assertIn("Capital at risk", dialogues[0])


class ClaudeRequestTests(unittest.TestCase):
    def test_ask_claude_request_and_parse(self):
        captured = {}
        payload = {"clips": [clip(1, 4, "Lost city")]}

        def create(**kwargs):
            captured.update(kwargs)
            return SimpleNamespace(stop_reason="end_turn",
                                   content=[SimpleNamespace(type="text", text=json.dumps(payload))])

        fake = SimpleNamespace(beta=SimpleNamespace(messages=SimpleNamespace(create=create)))
        cues = [cs.Cue(1, 0, 4, "Hello world.")]
        result = cs.ask_claude(cues, 5, 20, 90, "claude-opus-5-5", client=fake)
        self.assertEqual(result, payload)
        self.assertEqual(captured["model"], "claude-opus-5-5")
        self.assertEqual(captured["fallbacks"], "default")
        self.assertEqual(captured["betas"], ["server-side-fallback-2026-07-01"])
        self.assertEqual(captured["output_config"]["format"]["type"], "json_schema")
        self.assertIn("#1 [00:00:00.000 -> 00:00:04.000] Hello world.", captured["messages"][0]["content"])
        self.assertIn("review channel", captured["system"])

    def test_refusal_raises(self):
        fake = SimpleNamespace(beta=SimpleNamespace(messages=SimpleNamespace(
            create=lambda **k: SimpleNamespace(stop_reason="refusal", content=[]))))
        with self.assertRaises(RuntimeError):
            cs.ask_claude([cs.Cue(1, 0, 1, "x")], 1, 20, 90, "claude-opus-5-5", client=fake)


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "cần ffmpeg")
class RenderTests(unittest.TestCase):
    def test_end_to_end_with_plan(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            video = d / "long.mp4"
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "testsrc2=size=1920x1080:rate=24:duration=46",
                            "-f", "lavfi", "-i", "sine=frequency=330:duration=46", "-shortest",
                            "-c:v", "libx264", "-preset", "ultrafast", "-c:a", "aac", str(video)], check=True)
            srt = write_srt(d)
            plan = d / "plan.json"
            plan.write_text(json.dumps({"clips": [clip(1, 4, "Ubar found"), clip(5, 7, "Sinkhole")]}), encoding="utf-8")
            out = d / "out"
            for mode in ("crop", "blur"):
                extra = ["--note", "Not financial advice · Capital at risk"] if mode == "blur" else []
                rc = cs.main([str(video), str(srt), "--out", str(out / mode), "--plan", str(plan), "--mode", mode] + extra)
                self.assertEqual(rc, 0)
                info = json.loads(subprocess.run(
                    ["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height:format=duration",
                     "-of", "json", str(out / mode / "short_01.mp4")], check=True, capture_output=True, text=True).stdout)
                v = next(s for s in info["streams"] if s["codec_type"] == "video")
                self.assertEqual((v["width"], v["height"]), (1080, 1920))
                self.assertTrue(any(s["codec_type"] == "audio" for s in info["streams"]))
                self.assertAlmostEqual(float(info["format"]["duration"]), 22.35, delta=0.2)
                rows = (out / mode / "shorts.csv").read_text(encoding="utf-8-sig").splitlines()
                self.assertEqual(len(rows), 3)


if __name__ == "__main__":
    unittest.main()
