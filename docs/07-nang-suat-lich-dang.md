# 07 — Năng suất: mỗi ngày làm được bao nhiêu video & lịch đăng

> Số liệu từ sheet **NangSuat** và **LichDang** của [bảng tính](../ke-hoach/bang-tinh-ngan-sach-va-van-hanh.xlsx). Giả định 1 người, 7 giờ làm hiệu quả/ngày (420 phút), video review ~18 phút.

## 1. Thời gian cho 1 video review dài (cấp Tiêu chuẩn)

| # | Bước | Công cụ | Tháng đầu (phút) | Thành thạo (phút) |
|---|---|---|---|---|
| 1 | Chọn sản phẩm & nghiên cứu | Claude + skill affiliate research | 45 | 25 |
| 2 | Dùng thử & quay màn hình (dữ liệu thật) | OBS / Claude in Chrome | 60 | 40 |
| 3 | Kịch bản module + shot list + tuân thủ | Claude (skill) | 45 | 25 |
| 4 | **CỔNG 1** — duyệt kịch bản & tuân thủ | Người + Claude | 20 | 10 |
| 5 | Giọng đọc ~18 phút | ElevenLabs | 25 | 12 |
| 6 | Người dẫn AI *(Kênh B bỏ qua)* | HeyGen | 30 | 15 |
| 7 | Cảnh người thật AI + ảnh | Veo 3.1 / Nano Banana Pro | 45 | 25 |
| 8 | Dựng: màn hình, zoom, bảng giá, phụ đề | CapCut Pro | 100 | 55 |
| 9 | Thumbnail + SEO + link affiliate + disclosure | Claude + Nano Banana Pro | 30 | 15 |
| 10 | **CỔNG 2** — QC, xuất, hẹn giờ | Người + checklist | 20 | 12 |
| | **Tổng / 1 video dài** | | **420 phút (7 giờ)** | **234 phút (3,9 giờ)** |
| + | Cắt 5 short + duyệt + hẹn giờ | Tool Claude / OpusClip | 40 | 25 |
| + | 1 short native dọc | Claude + HeyGen/Veo + CapCut | 45 | 30 |

Kênh B nhanh hơn ~15 phút/video (không bước 6) nhưng bước 2 lâu hơn khi test nạp/rút. **Mốc kiểm tra: cuối tuần 4 phải ≤ 280 phút/video.**

## 2. Mỗi ngày ra được tối thiểu / tối đa bao nhiêu video

| Mức | Khi nào | Video dài / ngày | Short / ngày | % thời gian | Thời gian còn lại dùng cho |
|---|---|---|---|---|---|
| **TỐI THIỂU** | Tuần 1–4 | **0,5** (≈ 2–3 video/tuần) | 2–3 short cắt | 55% | Học công cụ, template, xin duyệt affiliate, chuẩn bị Kênh B |
| **TIÊU CHUẨN** | Từ tháng 2 | **1** (5 video/tuần, chia 2 kênh) | 5 short cắt + 1 short riêng = **6** | 69% | Phân tích số liệu, trả lời bình luận, cập nhật giá/link video cũ |
| **TỐI ĐA** | 1 người thành thạo | **1,5** | 7–8 short cắt | 93% | Không còn — chỉ để làm kho dự trữ |

Năng lực trần: 420 ÷ (234 + 25) = **~1,6 video dài/ngày** khi thành thạo (~0,9 ở tháng đầu).

Video review cần thêm thời gian **bảo trì**: cập nhật bình luận ghim khi giá sản phẩm đổi, thay link affiliate hết hạn — đây là lý do giữ ~30% thời gian dự phòng ở mức Tiêu chuẩn.

### So sánh: HeyGen Video Agent + trình dựng (Kênh A, sheet NangSuat)

| Hạng mục | Hiện tại · tháng đầu | Hiện tại · thành thạo | HeyGen · tháng đầu | HeyGen · thành thạo |
|---|---|---|---|---|
| Bước 1–4 (nghiên cứu, test & quay màn hình, kịch bản, Cổng 1) | 170 | 100 | 170 | 100 |
| Bước 5–8 (giọng, người dẫn, B-roll, dựng) | 200 | 107 | **110** ⚠️ | **60** ⚠️ |
| Bước 9–10 (thumbnail/SEO, Cổng 2) | 50 | 27 | 50 | 27 |
| **Tổng phút / video** | **420** | **234** | **330** | **187** |
| Video dài / ngày / người (kèm cắt short) | 0,9 | 1,6 | 1,1 | 2,0 |

⚠️ Phút bước 5–8 của HeyGen là **ước tính** — bấm giờ thật ở video thử #2 (20/10) rồi nhập vào ô NangSuat!E41:F41.

Tiết kiệm ~20% (90 phút/video tháng đầu, 47 phút khi thành thạo) ≈ **9,4 giờ/tháng** ở gói B. Kênh A vẫn giữ nhịp ~3 video/tuần, nên thời gian dư dùng để test sản phẩm kỹ hơn hoặc làm kho Kênh B, không phải để đăng nhiều hơn. Chi phí tiền ở [06 mục 7](06-ngan-sach.md#7-phương-án-heygen-video-agent--trình-dựng-chỉ-kênh-a-q9).

### Dây chuyền bán tự động (sheet NangSuat, mục Bán tự động)

| Bước | Hiện tại · thành thạo | Bán tự động | Ai làm |
|---|---|---|---|
| 1. Chọn sản phẩm | 25 | 5 | Claude chạy theo lịch; người duyệt danh sách |
| 2. Test & quay màn hình | 40 | **40** | **Người — bắt buộc** |
| 3. Kịch bản | 25 | 0 | AI |
| Cổng 1 | 10 | **10** | **Người** |
| 4. Giọng | 12 | 2 | ElevenLabs API |
| 5. Người dẫn | 15 | 3 | HeyGen API |
| 6. Cảnh Veo + ảnh | 25 | 15 | Claude soạn prompt; người tạo trong Flow |
| 7. Dựng | 55 | 30 | Máy ráp bản thô; người sửa |
| 8. Thumbnail + SEO | 15 | 5 | Claude; người chọn thumbnail |
| Cổng 2 | 12 | **12** | **Người** |
| **Tổng / video** | **234** | **~122** ⚠️ | |
| Cắt 5 short | 25 | 10 | Tool chạy sẵn; người duyệt |

Tiết kiệm ~127 phút/video Kênh A, ~115 phút/video Kênh B → **~41 giờ/tháng** ở gói B. Năng lực máy ~3,2 video dài/ngày/người, nhưng số đăng vẫn theo trần đăng và thời gian test. Giờ dư dùng để test kỹ hơn, làm Kênh B, hoặc gánh sản lượng gói C (40 video/tháng ≈ 108 giờ, kể cả short native) mà chưa cần người thứ 2 ⚠️ kiểm chứng sau GĐ2. Chi tiết: [11 mục 8](11-tich-hop-claude.md#8-dây-chuyền-tự-động-hằng-ngày--bán-tự-động-q10).

## 3. Trần đăng mỗi kênh

| Nền tảng | Loại | Tối thiểu | Tối đa | Gói B thực tế |
|---|---|---|---|---|
| YouTube | Video dài ≥ 15 phút | 2/tuần | 1/ngày | Kênh A ~3/tuần, Kênh B ~2/tuần |
| YouTube | Shorts | 1/ngày | 4/ngày | Kênh A ~2–3/ngày, Kênh B ~1–2/ngày |
| TikTok | Video dọc | 1/ngày | 3/ngày | Chỉ Kênh A (thử 30 ngày) |
| Facebook / Instagram | Reels | 1/ngày | 2/ngày | Kênh A; Kênh B hạn chế |

## 4. Lịch đăng: giờ Việt Nam ↔ giờ khán giả

Từ **01/11/2026** giờ VN sớm hơn New York **12 tiếng** (đến 14/03/2027), sớm hơn Paris 6 tiếng.

| Kênh · nền tảng | Loại | **Giờ VN** | New York | Paris | Tần suất |
|---|---|---|---|---|---|
| A · YouTube | Video dài | **02:00** | 14:00 | 20:00 | T3, T5, T7 |
| B · YouTube | Video dài | **03:00** | 15:00 | 21:00 | T2, T4 |
| A · YouTube | Short #1 | 21:00 | 09:00 | 15:00 | Hằng ngày |
| A · YouTube | Short #2 | 01:00 | 13:00 | 19:00 | Hằng ngày |
| B · YouTube | Short #1 | 23:00 | 11:00 | 17:00 | Hằng ngày |
| B · YouTube | Short #2 | 07:00 | 19:00 | 01:00 | Hằng ngày |
| A · TikTok | Short | 06:00 | 18:00 | 00:00 | 1–2/ngày |
| A · Facebook/Instagram | Reels | 00:00 | 12:00 | 18:00 | Hằng ngày |

Tất cả **hẹn giờ trước** trong YouTube Studio / Meta Business Suite — không ai phải thức đêm.

## 5. Nhịp làm việc mẫu 1 tuần (mức Tiêu chuẩn)

| Ngày | Sáng | Chiều |
|---|---|---|
| **Thứ Hai** | Claude phân tích số liệu tuần trước (views + click/chuyển đổi affiliate) → chọn 5 sản phẩm tuần → xin/kiểm tra affiliate | Test & quay màn hình 2 sản phẩm |
| Thứ Ba | Viết 5 kịch bản (Claude) → **Cổng 1** cả 5 | Test & quay màn hình 3 sản phẩm còn lại |
| Thứ Tư | Video A1: giọng → người dẫn → B-roll → dựng | A1: SEO → **Cổng 2** → hẹn giờ; cắt short; bắt đầu B1 |
| Thứ Năm | B1 hoàn tất; A2 | A2 hoàn tất; short |
| Thứ Sáu | A3 + B2 | 5 short native tuần sau; cập nhật giá/link video cũ; tổng kết lỗi → sửa Bible |

Gom việc theo loại (test 1 lượt, viết 1 lượt, duyệt 1 lượt) giúp giữ giọng văn đồng nhất và ít lỗi hơn.
