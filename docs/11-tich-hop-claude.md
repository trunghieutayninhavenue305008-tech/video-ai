# 11 — Tích hợp Claude: "bộ não" của xưởng video

> Claude không chỉ viết kịch bản. Trong quy trình này Claude là **trưởng nhóm nội dung + biên tập viên tiếng Anh bản ngữ + kiểm duyệt viên + kỹ sư tự động hoá**. Con người ra quyết định; Claude làm phần nặng.

## 1. Claude làm gì ở từng bước

| Bước | Claude làm | Hình thức dùng |
|---|---|---|
| 1. Chủ đề | Đề xuất & chấm điểm chủ đề, tìm nguồn có link (web search) | Claude Project của kênh |
| 2. Kịch bản | Viết kịch bản module + shot list + prompt ảnh/video + từ điển phát âm | **Skill `kich-ban-video`** |
| Cổng 1 | Soát sự thật, ngữ pháp, văn phong "AI", rủi ro chính sách, độ độc lập từng chương | **Skill `qc-video`** |
| 3–5. Giọng/ảnh/clip | Viết prompt chuẩn theo Bible; sửa prompt khi kết quả lỗi ("ảnh này bị lỗi tay, viết lại prompt") | Claude Project |
| 7. SEO | Tiêu đề, mô tả, chapter, hashtag, bình luận ghim, caption short từng nền tảng, chữ trên thumbnail | **Skill `seo-xuat-ban`** |
| 8. Cắt short | Đọc phụ đề, chọn 5 đoạn hay nhất, viết tiêu đề/hashtag; ffmpeg cắt tự động | **Claude API** qua `tools/cat_short.py` |
| 10. Phân tích | Đọc CSV YouTube Studio → báo cáo 5 dòng + 3 việc tuần tới | Claude Project |
| Bảo trì | Cập nhật Bible, skill, template khi có lỗi lặp lại; sửa tool | **Claude Code** trên repo này |

## 2. Gói Claude nên dùng

| Gói | Giá | Dùng khi |
|---|---|---|
| Pro | US$20/tháng | Tuần chuẩn bị (gói A) |
| **Max 5x** | **US$100/tháng** | **Gói B** — 1 người, 5 video/tuần, chạy nhiều phiên nghiên cứu + Claude Code |
| Max 20x | US$200/tháng | Gói C — 2 người/2 kênh |
| Claude API | Trả theo token | Tool tự động; Opus 5.5 giá US$4 / US$20 mỗi 1 triệu token vào/ra — cắt short cho 1 video tốn vài cent |

Hạn mức gói Pro/Max tính theo cửa sổ 5 giờ; Max 5x/20x gấp 5/20 lần Pro.

## 3. Thiết lập Claude Project cho kênh (làm 1 lần, 20 phút)

1. claude.ai → **Projects** → **Create project** → tên: `Kênh 1 — [Tên kênh]`.
2. **Project knowledge** — tải lên:
   - `templates/kenh-bible.md` (đã điền cho kênh)
   - `templates/thu-vien-prompt.md`
   - `templates/checklist-qc.md`
   - 2–3 kịch bản tốt nhất của kênh (bổ sung dần — Claude học giọng văn từ đây)
3. **Project instructions** — dán nguyên khối sau:

```text
Bạn là trưởng nhóm nội dung của kênh YouTube tiếng Anh "[Tên kênh]" (ngách: Lịch sử & Bí ẩn, khán giả toàn cầu).
- Luôn tuân thủ Bible kênh trong Project knowledge (giọng văn, phong cách hình, từ cấm, phát âm).
- Nội dung xuất bản viết bằng tiếng Anh Mỹ tự nhiên; giải thích, ghi chú và câu hỏi cho đội ngũ viết bằng tiếng Việt.
- Mọi khẳng định sự thật phải có nguồn kiểm chứng được; điều chưa chắc chắn thì nói rõ ("historians believe...").
- Không tạo nội dung: tài chính/y tế/pháp lý dưới dạng nhân vật chuyên gia AI; tin tức nóng; deepfake người thật; nội dung thao túng cảm xúc.
- Khi viết kịch bản, dùng skill kich-ban-video; khi soát lỗi dùng qc-video; khi làm tiêu đề/mô tả dùng seo-xuat-ban.
- Nếu yêu cầu mơ hồ, chọn phương án hợp lý nhất theo Bible và ghi rõ giả định thay vì hỏi lại.
```

## 4. Cài 3 skill của repo

Skill là "quy trình đóng gói" — Claude tự áp dụng đúng khuôn mỗi lần, nên đầu ra **không lệch giữa các video** (đây là cách chặn lỗi lặt vặt ở gốc).

| Skill | Thư mục | Đầu ra |
|---|---|---|
| `kich-ban-video` | [.claude/skills/kich-ban-video](../.claude/skills/kich-ban-video/SKILL.md) | Kịch bản module, shot list CSV, prompt ảnh/video, từ điển phát âm, 5 chương làm short |
| `qc-video` | [.claude/skills/qc-video](../.claude/skills/qc-video/SKILL.md) | Bảng lỗi theo mã + bản sửa đề xuất + kết luận Đạt/Không đạt |
| `seo-xuat-ban` | [.claude/skills/seo-xuat-ban](../.claude/skills/seo-xuat-ban/SKILL.md) | 3 tiêu đề, mô tả có chapter, tag, chữ thumbnail, caption short 4 nền tảng |

**Cài trên claude.ai:** nén từng thư mục skill thành file `.zip` (ví dụ `kich-ban-video.zip` chứa thư mục `kich-ban-video/` có `SKILL.md`) → **Settings → Capabilities → Skills → Upload skill**.

**Dùng với Claude Code:** mở terminal trong thư mục repo, chạy `claude` — các skill trong `.claude/skills/` tự được nạp.

## 5. Claude Code — tự động hoá không cần biết lập trình

Claude Code chạy trên máy (hoặc trên web claude.ai/code) và làm việc trực tiếp với file trong repo/Drive. Ví dụ câu lệnh có thể gõ bằng tiếng Việt:

- *"Chạy tools/cat_short.py cho video V007, chế độ blur, rồi mở shorts.csv cho tôi xem."*
- *"Đọc file analytics tuần này trong thư mục bao-cao/, so với 3 tuần trước, viết báo cáo 5 dòng theo mẫu ở docs/10."*
- *"Tuần này có 3 lỗi phụ đề ngắt dòng xấu. Sửa skill kich-ban-video và Bible để tránh lỗi này."*
- *"Tạo shot list cho 5 kịch bản trong thư mục tuần 45, xuất thành 5 file CSV."*

## 6. Tool `cat_short.py` (Claude API + ffmpeg)

Đầu vào: video dài + phụ đề SRT. Claude chọn 5 đoạn 20–90 giây đứng độc lập được, có câu mở mạnh và câu kết chốt → ffmpeg cắt sang 9:16 (cắt giữa hoặc nền mờ) + cháy phụ đề + xuất `shorts.csv` (tiêu đề, mô tả, hashtag từng nền tảng). Chi tiết cài đặt và cách chạy: [tools/README.md](../tools/README.md).

Chi phí: 1 video 10 phút ≈ 2.500 từ phụ đề ≈ vài nghìn token → **dưới US$0,10/video** với Opus 5.5.

## 7. Nguyên tắc dùng Claude để ít phải sửa

1. **Đưa đủ ngữ cảnh 1 lần** (Bible + brief) thay vì sửa qua lại nhiều lượt.
2. **Yêu cầu đầu ra có cấu trúc** (bảng, CSV) — skill đã làm sẵn.
3. **Bắt Claude tự soát trước khi đưa** — skill `qc-video` chạy trước khi người duyệt.
4. **Sửa ở gốc**: lỗi lặp lại → sửa skill/Bible, không sửa tay từng video.
5. **Không dán mật khẩu, API key, thông tin thẻ vào chat.** API key để trong biến môi trường `ANTHROPIC_API_KEY`.
