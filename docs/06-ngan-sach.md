# 06 — Ngân sách cho mỗi video & mỗi tháng

> Mọi con số dưới đây lấy từ [bảng tính](../ke-hoach/bang-tinh-ngan-sach-va-van-hanh.xlsx) (sheet **ChiPhiVideo**, **CongCu**, **HoaVon**). Đổi giả định ở sheet **ThongSo** → con số tự cập nhật. Tỷ giá lập kế hoạch: **26.500 ₫/USD**.

## 1. Ba cấp chất lượng cho 1 video dài 10 phút

| Tham số | Tiết kiệm | **Tiêu chuẩn (mặc định)** | Cao cấp |
|---|---|---|---|
| Tỷ lệ cảnh chuyển động AI (còn lại là ảnh tĩnh + zoom/pan) | 30% | **60%** | 90% |
| Hệ số làm lại (tạo bao nhiêu clip để được 1 clip dùng) | 2 | **2,5** | 3 |
| Mix model Veo 3.1 (Lite / Fast / Quality) | 70 / 30 / 0 | **40 / 60 / 0** | 0 / 80 / 20 |
| Số clip 8 giây phải tạo | 45 | **113** | 203 |
| Credit Flow / video (gói Ultra) | 293 | **900** | 5.670 |
| Số ảnh phải tạo | 185 | **170** | 155 |
| Ký tự giọng đọc (gồm đọc lại) | 11.700 | **11.700** | 11.700 |
| Dùng cho | Video thường ngày, chủ đề nhẹ | **Mọi video chính** | Video "flagship" 1–2 lần/tháng |

## 2. Chi phí biến đổi cho 1 video dài — thuê bao vs trả theo lượt (API)

| | Tiết kiệm | **Tiêu chuẩn** | Cao cấp |
|---|---|---|---|
| **Tuyến thuê bao (đề xuất)** — video + ảnh + giọng | **US$4,1** (~110 nghìn ₫) | **US$8,7** (~231 nghìn ₫) | **US$44,7** (~1,19 triệu ₫) |
| Tuyến API trả theo lượt (tham chiếu) | US$60,8 (~1,61 triệu ₫) | US$119,3 (~3,16 triệu ₫) | US$308,8 (~8,18 triệu ₫) |
| **API đắt gấp** | **14,7 lần** | **13,7 lần** | **6,9 lần** |

→ **Quyết định: sản xuất bằng thuê bao, chỉ dùng API cho tự động hoá nhỏ (Claude API cắt short).**

*Chi phí biến đổi chưa gồm các công cụ cố định (Claude, CapCut, Suno, OpusClip) — phần đó tính trong "chi phí trọn gói" bên dưới.*

## 3. Ba gói ngân sách theo tháng

| Công cụ | Gói A — Thử nghiệm | **Gói B — Tiêu chuẩn** | Gói C — Mở rộng |
|---|---|---|---|
| Claude | Pro US$20 | **Max 5x US$100** | Max 20x US$200 |
| Claude API | — | **US$10** | US$30 |
| Google AI (Veo 3.1 + Nano Banana Pro) | AI Pro US$19,99 | **AI Ultra 20x US$199,99** | 2 × Ultra 20x US$399,98 |
| Kling | — | **Standard US$10** | Pro US$37 |
| ElevenLabs | Creator US$22 | **Pro US$99** | 2 × Pro US$198 |
| CapCut Pro | US$10 | **US$10** | 2 × US$10 |
| Suno | — | **Pro US$10** | Premier US$30 |
| OpusClip | — (dùng tool Claude) | **Pro US$29** | 2 × Pro US$58 |
| YouTube Audio Library | 0 | **0** | 0 |
| **Cộng** | US$71,99 | **US$467,99** | US$972,98 |
| Dự phòng 10% (thuế, tỷ giá, mua thêm credit) | US$7,20 | **US$46,80** | US$97,30 |
| **TỔNG / THÁNG** | **~US$79 ≈ 2,1 triệu ₫** | **~US$515 ≈ 13,6 triệu ₫** | **~US$1.070 ≈ 28,4 triệu ₫** |

### Sản lượng & chi phí trọn gói

| | Gói A | **Gói B** | Gói C |
|---|---|---|---|
| Cấp chất lượng | Tiết kiệm | **Tiêu chuẩn** | Tiêu chuẩn |
| Video dài / tháng | 4 | **20** | 44 |
| Short cắt (5/video dài) | 20 | **100** | 220 |
| Short native | 0 | **20** | 20 |
| **Tổng sản phẩm đăng / tháng** | 24 | **140** | 284 |
| Credit Flow cần / có | 2.340 / 2.500 ✅ | **20.813 / 26.500 ✅** | 42.413 / 53.000 ✅ |
| **Chi phí trọn gói / 1 video dài (kèm các short của nó)** | US$19,8 ≈ 525 nghìn ₫ | **US$25,7 ≈ 682 nghìn ₫** | US$24,3 ≈ 645 nghìn ₫ |
| Chi phí bình quân / 1 sản phẩm đăng | US$3,30 ≈ 87 nghìn ₫ | **US$3,68 ≈ 97 nghìn ₫** | US$3,77 ≈ 100 nghìn ₫ |
| Nhân sự | 1 người | **1 người** | 2 người |

**Trả lời thẳng câu hỏi "ngân sách mỗi video":**
- **Video dài 10 phút (kèm 5 short cắt từ nó): ~US$26 ≈ 680 nghìn ₫** (gói B, đã gồm mọi thuê bao).
- **Chi phí phát sinh thêm khi làm thêm 1 video dài** (khi còn credit): **~US$9 ≈ 230 nghìn ₫**.
- **Short native:** ~140 credit ≈ **US$1 ≈ 28 nghìn ₫**.
- **Video "flagship" cấp Cao cấp:** ~**US$45 ≈ 1,2 triệu ₫** phát sinh.

## 4. Lộ trình chi tiêu đề xuất

| Thời gian | Gói | Chi phí ước tính |
|---|---|---|
| Tuần chuẩn bị (15–21/10): thiết lập + 2 video thử | A | ~2,1 triệu ₫ (cả tháng) |
| Từ ngày ra mắt 22/10 nếu 2 video thử đạt chuẩn ở Cổng 2 | Nâng lên B (trả chênh lệch) | ~13,6 triệu ₫/tháng |
| Từ tháng thứ 4 nếu đạt YPP và KPI | Cân nhắc C (kênh 2 hoặc lồng tiếng) | ~28,4 triệu ₫/tháng |

**Tổng ngân sách công cụ 3 tháng đầu (đến 31/01/2027): ~2,1 + 3 × 13,6 ≈ 43 triệu ₫** (chưa gồm nhân sự).

## 5. Điểm hoà vốn (sheet **HoaVon**)

Giả định (sửa được): RPM video dài **US$6** (thận trọng — trung vị ngách Giáo dục & Khoa học là US$10,22 theo AIR Media-Tech), RPM Shorts **US$0,05**, gói B, chi phí nhân sự **15 triệu ₫/tháng** (giả định — thay bằng số thực).

| Chỉ tiêu | Kết quả |
|---|---|
| Lượt xem / video dài / tháng để **hoà vốn chi phí công cụ** | **~4.100** |
| Lượt xem / video dài / tháng để **hoà vốn cả công cụ + nhân sự** | **~8.900** |
| Ví dụ: 5.000 lượt xem/video dài, 3.000/short | Doanh thu ~US$618/tháng; lỗ ~12,3 triệu ₫ nếu tính lương, **lãi nhẹ nếu chỉ tính công cụ** |

**Lưu ý trung thực:**
- Doanh thu quảng cáo chỉ có **sau khi vào YPP** (mục tiêu trước 31/01/2027). 3 tháng đầu là giai đoạn **đầu tư**.
- Video "xanh mãi" tiếp tục kiếm view nhiều năm → doanh thu cộng dồn theo thư viện video, không chỉ video mới.
- Nhiều kênh mới không bao giờ đạt YPP. Kế hoạch giảm rủi ro bằng: chọn ngách có cầu, đo KPI hằng tuần, **điểm dừng ở ngày 60** (xem [10](10-kpi-lo-trinh.md)).

## 6. Rủi ro chi phí & cách phòng

| Rủi ro | Phòng ngừa |
|---|---|
| Công cụ tăng giá / đổi chính sách credit | Bảng tính cập nhật trong 5 phút; luôn có công cụ dự phòng cho mỗi bước |
| Gói Ultra chưa mở tại VN | AI Pro + Kling Pro + Seedance (chi phí/giây cao hơn ~3–5 lần, vẫn rẻ hơn API) |
| Tạo lại nhiều hơn dự kiến (hệ số làm lại cao) | Theo dõi hệ số thực tế 2 tuần đầu, chỉnh ô ThongSo!B21 |
| Credit tháng không cộng dồn | Ưu tiên dùng credit theo ngày trước; làm kho dự trữ short native khi dư credit cuối tháng |
| Chênh tỷ giá, phí thẻ quốc tế | Dự phòng 10% đã gồm |
