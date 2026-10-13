# 08 — Hệ thống chống lỗi lặt vặt ("làm đúng ngay từ đầu")

> Yêu cầu: **hạn chế tối đa việc sửa những lỗi nhỏ nhặt.** Cách làm: **chặn lỗi từ gốc** — mỗi lỗi chỉ được xảy ra 1 lần; lần thứ 2 phải bị chặn bằng Bible, skill, template hoặc checklist. Với kênh review, "lỗi nhỏ" còn có thể là **lỗi pháp lý** (thiếu công khai affiliate, sai giá, câu hứa hẹn) — nên được chặn ngay ở kịch bản.

## 1. Năm lớp phòng thủ

| Lớp | Công cụ | Chặn loại lỗi nào |
|---|---|---|
| **1. Bible kênh** ([mẫu](../templates/kenh-bible.md)) | Giọng văn, người dẫn, phong cách hình, câu công khai chuẩn, từ cấm, phát âm tên sản phẩm | Lệch phong cách, thiếu công khai, sai phát âm |
| **2. Skill Claude** ([.claude/skills](../.claude/skills/)) | `kich-ban-video`, `qc-video`, `seo-xuat-ban` — đầu ra đúng khuôn, có sẵn câu công khai & cảnh báo | Kịch bản thiếu phần, câu bịa trải nghiệm, tiêu đề quá dài, mô tả thiếu disclosure |
| **3. Template & preset** | Template CapCut cho từng loại phần (tính năng, bảng giá, so sánh, kết luận), preset xuất, thư viện prompt | Sai khung hình, sai font, bảng giá lệch mẫu, âm lượng không đều |
| **4. Hai cổng duyệt** ([checklist](../templates/checklist-qc.md)) | Cổng 1 (kịch bản + tuân thủ) + Cổng 2 (video + xuất bản) | Lỗi lọt qua 3 lớp trên |
| **5. Nhật ký lỗi → sửa gốc** | Cột "Lỗi ở Cổng 2" + "Nguyên nhân gốc" trong sheet **TheoDoi** | Lỗi lặp lại |

**Quy tắc vàng:** lỗi lặp ≥ 2 lần/tuần → thứ Sáu sửa Bible/skill/template. Mục tiêu: **< 10% video phải sửa sau Cổng 2**, **0 video thiếu công khai**.

## 2. Vì sao Cổng 1 quan trọng nhất

| Sửa ở đâu | Chi phí sửa 1 lỗi |
|---|---|
| Kịch bản (Cổng 1) | ~10 giây, 0 credit |
| Sau khi tạo giọng | ~3 phút |
| Sau khi tạo người dẫn AI / B-roll | ~15 phút + credit HeyGen/Veo |
| Sau khi dựng xong video 18 phút | ~30–45 phút |
| Sau khi đăng | Không sửa được video; lỗi pháp lý (thiếu công khai, hứa lợi nhuận) có thể gây gậy cảnh cáo/phạt |

## 3. Top 25 lỗi hay gặp ở video review AI & cách chặn từ gốc

| # | Lỗi | Phát hiện ở | Cách chặn từ gốc |
|---|---|---|---|
| L1 | AI vẽ chữ sai trong ảnh/video | Cổng 2 | Prompt luôn có `no text, no logos`; chữ/logo thêm ở CapCut |
| L2 | Ngón tay/thân thể người AI biến dạng | Cổng 2 | Shot list tránh cận tay; dùng trung cảnh; tạo 2–3 bản chọn bản tốt |
| L3 | Người dẫn đổi mặt/đổi trang phục giữa video | Cổng 2 | 1 Avatar ID cố định trong Bible; không tạo lại avatar mỗi video |
| L4 | Giọng đọc sai tên sản phẩm (HubSpot, cTrader, Bybit…) | Bước 5 | Từ điển phát âm trong Bible; skill chèn phiên âm vào bản đọc |
| L5 | Đọc sai số/giá ("$29.99/mo") | Bước 5 | Skill viết số thành chữ trong bản đọc ("twenty-nine ninety-nine a month") |
| L6 | Phụ đề sai chính tả, ngắt dòng xấu | Cổng 2 | Phụ đề lấy từ kịch bản; preset ≤ 42 ký tự/dòng, 2 dòng |
| L7 | Âm lượng chênh nhau | Cổng 2 | Preset -14 LUFS |
| L8 | Nhạc át giọng | Cổng 2 | Ducking trong template |
| L9 | Âm thanh lạ từ clip Veo | Bước 7 | Tắt tiếng clip Veo; prompt có `no dialogue, no music` |
| L10 | Khung đen, khoảng trống timeline | Cổng 2 | Magnetic timeline; tua 2x trước khi xuất |
| L11 | Short sai khung hình | Sau đăng | Tool `cat_short.py` luôn xuất 1080×1920 |
| L12 | Chữ short bị nút bấm che | Sau đăng | Vùng an toàn trong template; tool chừa lề phải |
| L13 | Tiêu đề > 60 ký tự | Bước 9 | Skill `seo-xuat-ban` giới hạn & đếm ký tự |
| L14 | Thumbnail chữ khó đọc | Bước 9 | ≤ 4 từ, kiểm tra ở 160 px |
| L15 | Sai thông tin sản phẩm (tính năng, giới hạn gói) | Cổng 1 | Chỉ khẳng định điều có trong `ghi-chu-test.md` hoặc trang chính thức có link |
| L16 | Văn phong AI sáo rỗng ("game-changer", "revolutionary"…) | Cổng 1 | Danh sách từ cấm trong Bible |
| L17 | Quên bật nhãn nội dung AI | Cổng 2 | Ô bắt buộc trong checklist (người dẫn AI → luôn bật) |
| L18 | Nhạc bị Content ID claim | Sau đăng | Chỉ YouTube Audio Library / Suno Pro |
| L19 | Mô tả thiếu chapter / link | Bước 9 | Skill xuất mô tả đúng khuôn |
| L20 | File lộn xộn | Mọi bước | Cấu trúc thư mục cố định |
| **L21** | **Thiếu/không rõ công khai affiliate** (chỉ để cuối mô tả) | Cổng 1 & 2 | Câu công khai chuẩn trong Bible: nói bằng lời ở 30 giây đầu + chữ trên hình + **dòng đầu** mô tả |
| **L22** | **Câu bịa trải nghiệm** ("I've used it for 6 months") | Cổng 1 | Skill chỉ dùng "we tested… for [số ngày thật]" theo ghi chú test; `qc-video` bắt lỗi C2 |
| **L23** | **Giá/khuyến mãi lỗi thời** | Cổng 1 & sau đăng | Mọi giá kèm "as of [tháng/năm]"; ghim bình luận cập nhật giá; Amazon: không nêu giá cụ thể, mời xem giá ở link |
| **L24** | **Kênh B: thiếu cảnh báo rủi ro / có câu như lời khuyên đầu tư** | Cổng 1 | Khối cảnh báo chuẩn trong Bible; danh sách cụm cấm ("guaranteed", "risk-free", "you should buy"…) |
| **L25** | **Link affiliate sai/hết hạn, link Kênh B không qua lọc quốc gia** | Cổng 2 | Mọi link qua trang trung gian của công ty; kiểm tra bằng checklist P-link |

## 4. "Định nghĩa hoàn thành" từng bước

| Bước | Hoàn thành khi |
|---|---|
| Chọn sản phẩm | Có brief, chương trình affiliate (đã duyệt/đang chờ), Kênh B: giấy phép cấp 1 đã tra trên trang cơ quan quản lý |
| Test & quay màn hình | Đủ cảnh theo danh sách; `ghi-chu-test.md` có số liệu + ảnh chụp bằng chứng |
| Kịch bản | Qua Cổng 1; có shot list; câu công khai & cảnh báo đúng chỗ; từ điển phát âm |
| Người dẫn AI | Đúng Avatar ID, khẩu hình khớp, không lỗi hình |
| Dựng | 1080p, -14 LUFS, phụ đề SRT, dòng công khai trên hình ở 30 giây đầu |
| SEO | Dòng đầu mô tả là công khai; tiêu đề ≤ 60 ký tự; giá có ngày; Kênh B: cảnh báo rủi ro |
| Short | 1080×1920, câu đầu độc lập; Kênh B có dòng cảnh báo cố định |

## 5. Ai sửa gì

- Người duyệt **chỉ đánh dấu Đạt/Không đạt + ghi mã lỗi** (K…, C…, V…, P…, S…, L…), không ngồi sửa tay.
- Lỗi tuân thủ (C…, L21–L25) **luôn là "Không đạt"** — không có ngoại lệ "sửa sau".
- Lỗi "khẩu vị" không phải lỗi — gom lại, quyết 1 lần, ghi vào Bible.
