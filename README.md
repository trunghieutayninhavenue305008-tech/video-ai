# Xưởng Video AI — Kế hoạch triển khai thị trường Global

Bộ hồ sơ đầy đủ để **review thứ Tư 14/10/2026** và **bắt tay sản xuất ngay sau đó**: chiến lược, quy trình 100% AI với Claude làm trung tâm, ngân sách có bảng tính, năng suất, chống lỗi lặt vặt, chính sách & pháp lý, lộ trình 90 ngày, kịch bản thuyết trình, mẫu dùng ngay, 3 skill Claude và công cụ tự động cắt short.

## Tóm tắt 30 giây

| | |
|---|---|
| **Thị trường** | Toàn cầu, kênh YouTube **tiếng Anh** — ngách đề xuất **Lịch sử & Bí ẩn** |
| **Định dạng** | Video dài **8–15 phút** (chuẩn 10–12) + Short **20–90 giây** (chuẩn 30–50) |
| **Mô hình** | Làm video dài trước → cắt **5 short** + 1 short làm riêng; kịch bản viết dạng module để cắt không phải sửa |
| **Công cụ** | **Claude** (não) · Veo 3.1/Flow · Nano Banana Pro · ElevenLabs · CapCut Pro · OpusClip / tool Claude |
| **Ngân sách đề xuất** | **~US$515 ≈ 13,6 triệu ₫/tháng** → 20 video dài + 120 short → **~682 nghìn ₫/video dài kèm 5 short** |
| **Năng suất (1 người)** | Tối thiểu 3 video dài/tuần · chuẩn 1 video dài + 6 short/ngày · tối đa 2 video dài/ngày |
| **Mục tiêu 90 ngày** | Ra mắt 22/10/2026 → **đạt điều kiện kiếm tiền YouTube trước 31/01/2027** (trước khi ngưỡng tăng gấp đôi) |

👉 Đọc trước: [docs/01-tom-tat-de-xuat.md](docs/01-tom-tat-de-xuat.md) (3 phút) và [docs/12-kich-ban-thuyet-trinh.md](docs/12-kich-ban-thuyet-trinh.md) (lời dẫn + 16 câu hỏi đáp).

## Nội dung repo

### Tài liệu kế hoạch — `docs/`
| # | Tài liệu | Trả lời câu hỏi |
|---|---|---|
| 01 | [Tóm tắt đề xuất](docs/01-tom-tat-de-xuat.md) | Đề xuất gì, vì sao bây giờ, cần chốt quyết định nào |
| 02 | [Thị trường, ngách, nền tảng](docs/02-thi-truong-ngach-nen-tang.md) | Vì sao Global tiếng Anh, ngách nào, nền tảng nào làm gì |
| 03 | [Định dạng & độ dài](docs/03-dinh-dang-do-dai.md) | Độ dài tối thiểu/tối đa, dài hay short, làm dài rồi cắt short thế nào |
| 04 | [Quy trình sản xuất](docs/04-quy-trinh-san-xuat.md) | 100% AI từ làm đến cắt ghép, từng bước, ai làm gì |
| 05 | [Bộ công cụ](docs/05-bo-cong-cu.md) | Dùng tool nào, giá bao nhiêu, vì sao, không dùng tool nào |
| 06 | [Ngân sách](docs/06-ngan-sach.md) | Ngân sách mỗi video, mỗi tháng, hoà vốn |
| 07 | [Năng suất & lịch đăng](docs/07-nang-suat-lich-dang.md) | Mỗi ngày tối thiểu/tối đa bao nhiêu video, đăng giờ nào |
| 08 | [Chống lỗi lặt vặt](docs/08-chong-loi-lat-vat.md) | Làm sao hạn chế tối đa sửa lỗi nhỏ |
| 09 | [Chính sách, pháp lý, rủi ro](docs/09-chinh-sach-phap-ly-rui-ro.md) | YouTube/TikTok/Meta, Luật AI Việt Nam, thuế, ma trận rủi ro |
| 10 | [KPI & lộ trình](docs/10-kpi-lo-trinh.md) | Đo gì, 90 ngày làm gì, **7 ngày đầu sau review** |
| 11 | [Tích hợp Claude](docs/11-tich-hop-claude.md) | Claude làm gì ở từng bước, cài Project & skill |
| 12 | [Kịch bản thuyết trình](docs/12-kich-ban-thuyet-trinh.md) | Lời dẫn từng slide, con số cần thuộc, hỏi đáp |
| — | [Nguồn tham khảo](docs/nguon-tham-khao.md) | Link nguồn cho mọi số liệu |

### Bảng tính — `ke-hoach/`
[bang-tinh-ngan-sach-va-van-hanh.xlsx](ke-hoach/bang-tinh-ngan-sach-va-van-hanh.xlsx): mọi con số là **công thức** — sửa giả định (ô chữ xanh) là toàn bộ tự cập nhật. Gồm: ThongSo, CongCu (3 gói), ChiPhiVideo, NangSuat, HoaVon (+ mục tiêu YPP), LichDang, TheoDoi (theo dõi sản xuất), KPI.

### Mẫu dùng ngay — `templates/`
- [kenh-bible.md](templates/kenh-bible.md) — "hiến pháp" của kênh (đã điền ví dụ cho ngách Lịch sử & Bí ẩn)
- [brief-video.md](templates/brief-video.md) — brief cho từng video
- [checklist-qc.md](templates/checklist-qc.md) — checklist 2 cổng duyệt, có mã lỗi
- [thu-vien-prompt.md](templates/thu-vien-prompt.md) — prompt cho Claude, Nano Banana Pro, Veo 3.1, thumbnail, phân tích số liệu

### Skill Claude — `.claude/skills/`
- [kich-ban-video](.claude/skills/kich-ban-video/SKILL.md) — kịch bản module + bản đọc + shot list CSV + prompt + nguồn
- [qc-video](.claude/skills/qc-video/SKILL.md) — soát lỗi theo mã, kiểm sự thật, đề xuất sửa gốc
- [seo-xuat-ban](.claude/skills/seo-xuat-ban/SKILL.md) — tiêu đề, mô tả, chapter, thumbnail, caption short 4 nền tảng

Cài lên claude.ai hoặc dùng với Claude Code: xem [docs/11](docs/11-tich-hop-claude.md#4-cài-3-skill-của-repo).

### Công cụ — `tools/`
- [cat_short.py](tools/cat_short.py) — Claude chọn 5 đoạn hay từ phụ đề → ffmpeg cắt short 9:16 có phụ đề + `shorts.csv` caption. Hướng dẫn: [tools/README.md](tools/README.md).

## Bắt đầu ngay sau review
Làm theo **Kế hoạch 7 ngày** ở [docs/10](docs/10-kpi-lo-trinh.md#3-kế-hoạch-7-ngày-sau-buổi-review-bắt-tay-làm-ngay): 15/10 mở tài khoản → 16/10 Bible kênh → 19–20/10 hai video thử → 21/10 sếp duyệt → **22/10 ra mắt kênh**.

> Giá công cụ và chính sách nền tảng là ảnh chụp tháng 9–10/2026; các điểm đánh dấu ⚠️ trong tài liệu cần xác nhận lại trước khi áp dụng.
