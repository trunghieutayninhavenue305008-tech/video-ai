# Tool `cat_short.py` — Claude chọn đoạn hay, ffmpeg tự cắt short 9:16

Thay cho việc ngồi tua video review 15–20 phút tìm đoạn hay rồi cắt tay. Đầu vào là video dài đã dựng + file phụ đề SRT (xuất từ CapCut). Claude chọn 5 phần đứng độc lập (demo tính năng, bảng giá, so sánh, kết luận), bỏ qua phần công khai/kêu gọi, không chọn đoạn hứa hẹn lợi nhuận. Đầu ra là 5 short dọc 1080×1920 có phụ đề kiểu short (1–4 từ/lần hiện), âm lượng chuẩn -14 LUFS, (tuỳ chọn) dòng cảnh báo cố định cho Kênh B, kèm `shorts.csv` có sẵn tiêu đề & caption cho YouTube Shorts, TikTok, Instagram, Facebook.

## Cài đặt (1 lần)

1. **Python 3.10+** — https://www.python.org/downloads/ (Windows: tick "Add Python to PATH").
2. **ffmpeg** — Windows: `winget install Gyan.FFmpeg`; macOS: `brew install ffmpeg`.
3. Thư viện: `pip install -r tools/requirements.txt`
4. **API key Claude**: tạo tại https://console.anthropic.com → API Keys, rồi đặt biến môi trường (không dán key vào file/chat):
   - Windows (PowerShell): `setx ANTHROPIC_API_KEY "sk-ant-..."` rồi mở lại cửa sổ.
   - macOS/Linux: thêm `export ANTHROPIC_API_KEY="sk-ant-..."` vào `~/.zshrc` hoặc `~/.bashrc`.

## Cách dùng

```bash
# Chuẩn: Claude chọn 5 đoạn, cắt giữa khung (cảnh đã bố cục chủ thể ở giữa)
python tools/cat_short.py V001/8_export/final_16x9.mp4 V001/8_export/subtitles.srt --out V001/9_shorts

# Đoạn quay màn hình sản phẩm → dùng nền mờ (giữ nguyên giao diện ở giữa, phụ đề bên dưới)
python tools/cat_short.py final_16x9.mp4 subtitles.srt --out 9_shorts --mode blur

# Kênh B (Crypto & Forex): thêm dòng cảnh báo cố định suốt short
python tools/cat_short.py final_16x9.mp4 subtitles.srt --out 9_shorts --mode blur --note "Not financial advice · Capital at risk"

# Chỉ xem Claude chọn đoạn nào (không cắt) → sửa plan.json nếu muốn → cắt theo plan
python tools/cat_short.py final_16x9.mp4 subtitles.srt --out 9_shorts --plan-only
python tools/cat_short.py final_16x9.mp4 subtitles.srt --out 9_shorts --plan 9_shorts/plan.json
```

Tuỳ chọn khác: `--count 5` (số short), `--min 20 --max 90` (giây), `--words 4` (số từ mỗi lần hiện phụ đề), `--font "Montserrat ExtraBold" --font-size 78`, `--note "…"` (dòng chữ cố định phía trên), `--no-subs`, `--no-loudnorm`, `--model claude-opus-5-5`.

**Chọn chế độ:** đoạn người dẫn / cảnh người → `crop` (chủ thể ở giữa); đoạn quay màn hình → `blur` (cắt giữa sẽ mất giao diện). Nếu 5 short lẫn cả hai loại, chạy `--plan-only`, sửa `plan.json`, rồi chạy 2 lần với 2 chế độ cho từng nhóm.

## Đầu ra (thư mục `--out`)

| File | Nội dung |
|---|---|
| `short_01.mp4 … short_05.mp4` | Short 1080×1920, 30 fps, H.264/AAC, -14 LUFS, phụ đề cháy vào hình |
| `short_0N.ass` | File phụ đề + dòng cảnh báo đã định dạng (giữ lại để kiểm tra) |
| `plan.json` | Đoạn Claude chọn (số thứ tự dòng phụ đề đầu/cuối + tiêu đề, caption). **Sửa tay được.** |
| `shorts.csv` | Mở bằng Excel: thời điểm cắt, tiêu đề YouTube Shorts, caption TikTok/Instagram/Facebook, hashtag, câu đầu/câu cuối, lý do chọn |

## Tool tự kiểm tra gì

- Mỗi short dài trong khoảng `--min`…`--max` giây (tự nới/thu đoạn nếu Claude chọn lệch).
- Các short không trùng nhau.
- **Cảnh báo** nếu short mở đầu bằng từ nối ("And…", "But…", "This…") — dấu hiệu phần chưa đứng độc lập (lỗi K2 ở Cổng 1).

## Chi phí & dữ liệu

- Claude chỉ đọc **phụ đề** (không gửi video): ~vài nghìn token/video → **dưới US$0,10/video** với Opus 5.5 (US$4 / US$20 mỗi 1 triệu token vào/ra).
- Tool bật sẵn `fallbacks: "default"` (beta `server-side-fallback-2026-07-01`): nếu bộ lọc an toàn từ chối nhầm, API tự chạy lại trên model dự phòng trong cùng lần gọi. Nếu tài khoản chưa hỗ trợ, tool tự gọi lại không có tham số này.

## Kiểm thử

```bash
python -m unittest tools/test_cat_short.py -v
```
12 bài kiểm thử: đọc SRT (BOM, CRLF), chuẩn hoá plan, chia phụ đề, dòng cảnh báo `--note`, cấu trúc request gửi Claude (giả lập), và **cắt thật** 2 short bằng ffmpeg ở cả chế độ `crop` lẫn `blur` (có `--note`) — bỏ qua phần cắt thật nếu máy chưa có ffmpeg.
