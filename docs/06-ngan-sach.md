# 06 — Ngân sách cho mỗi video, mỗi tháng & điểm hoà vốn

> Số liệu từ [bảng tính](../ke-hoach/bang-tinh-ngan-sach-va-van-hanh.xlsx) (sheet **ChiPhiVideo**, **CongCu**, **DoanhThu**). Đổi giả định ở **ThongSo** → con số tự cập nhật. Tỷ giá lập kế hoạch: **26.500 ₫/USD**. Video dài lập ngân sách ở **18 phút**.

## 1. Cơ cấu hình ảnh & khối lượng cho 1 video dài 18 phút

| Tham số | A · Tiết kiệm | **A · Tiêu chuẩn** | A · Cao cấp | **B · Tài chính** |
|---|---|---|---|---|
| Người dẫn AI (HeyGen) | 15% | **20%** | 25% | **0%** |
| Cảnh người thật AI (Veo 3.1) | 15% | **20%** | 30% | **20%** |
| Quay màn hình / hình sản phẩm thật | 50% | **40%** | 30% | **55%** |
| Đồ hoạ (giá, so sánh) | 20% | **20%** | 15% | **25%** |
| Phút HeyGen phải tạo (gồm làm lại) | 3,5 | **4,7** | 5,9 | 0 |
| Clip Veo phải tạo | 41 | **68** | 122 | 68 |
| Credit Flow / video (Ultra) | 304 | **945** | 4.496 | 945 |
| Ký tự giọng đọc | 21.060 | **21.060** | 21.060 | 21.060 |

## 2. Chi phí biến đổi 1 video dài — thuê bao vs API

| | A · Tiết kiệm | **A · Tiêu chuẩn** | A · Cao cấp | **B · Tài chính** |
|---|---|---|---|---|
| Cảnh người AI (Veo) | US$2,3 | **US$7,1** | US$33,9 | US$7,1 |
| Người dẫn AI (HeyGen) | US$3,4 | **US$4,6** | US$5,7 | 0 |
| Giọng đọc | US$3,5 | **US$3,5** | US$3,5 | US$3,5 |
| **Cộng — tuyến thuê bao** | **US$9,2 ≈ 244 nghìn ₫** | **US$15,2 ≈ 403 nghìn ₫** | **US$43,1 ≈ 1,14 triệu ₫** | **US$10,6 ≈ 281 nghìn ₫** |
| Tuyến API (tham chiếu) | US$46,5 | US$87,3 | US$220,2 | US$82,7 |
| API đắt gấp | 5,1 lần | **5,7 lần** | 5,1 lần | 7,8 lần |

*Chưa gồm công cụ cố định (Claude, CapCut, Suno, OpusClip) và ngân sách dùng thử sản phẩm — phần đó nằm trong "chi phí trọn gói" bên dưới.*

## 3. Ba gói ngân sách theo tháng

| Công cụ | Gói A — Thử nghiệm | **Gói B — Tiêu chuẩn** | Gói C — Mở rộng |
|---|---|---|---|
| Claude | Pro US$20 | **Max 5x US$100** | Max 20x US$200 |
| Claude API | — | **US$10** | US$30 |
| Google AI (Veo 3.1 + Nano Banana Pro) | AI Pro US$19,99 | **Ultra 20x US$199,99** | 2 × Ultra 20x US$399,98 |
| HeyGen (người dẫn AI) | Creator US$29 | **Pro ~1.500 credit ~US$74\*** | Pro ~3.000 credit ~US$147\* |
| ElevenLabs | Creator US$22 | **Pro US$99** | 2 × Pro US$198 |
| Kling | — | **Standard US$10** | Pro US$37 |
| CapCut Pro | US$10 | **US$10** | 2 × US$10 |
| Suno | — | **Pro US$10** | Premier US$30 |
| OpusClip | — | **Pro US$29** | 2 × Pro US$58 |
| Ngân sách dùng thử sản phẩm | US$50 | **US$150** | US$300 |
| **Cộng** | US$150,99 | **US$691,99** | US$1.419,98 |
| Dự phòng 10% | US$15,10 | **US$69,20** | US$142,00 |
| **TỔNG / THÁNG** | **~US$166 ≈ 4,4 triệu ₫** | **~US$761 ≈ 20,2 triệu ₫** | **~US$1.562 ≈ 41,4 triệu ₫** |

\* Giá ước tính tuyến tính theo US$49/1.000 credit — xác nhận khi mua.

### Sản lượng, kiểm tra tài nguyên & chi phí trọn gói

| | Gói A | **Gói B** | Gói C |
|---|---|---|---|
| Video dài Kênh A + Kênh B / tháng | 4 + 0 | **12 + 8** | 24 + 16 |
| Short (5 cắt / video dài + short riêng) | 20 + 0 | **100 + 20** | 200 + 40 |
| **Tổng sản phẩm đăng / tháng** | 24 | **140** | 280 |
| Credit Flow cần / có | 2.430 / 2.500 ✅ | **21.713 / 26.500 ✅** | 43.425 / 53.000 ✅ |
| Credit HeyGen cần / có | 281 / 600 ✅ | **1.123 / 1.500 ✅** | 2.246 / 3.000 ✅ |
| Ký tự ElevenLabs cần / có | 84.240 / 121.000 ✅ | **438.750 / 600.000 ✅** | 877.500 / 1.200.000 ✅ |
| **Trọn gói / 1 video dài kèm các short** | US$41,5 ≈ 1,10 triệu ₫ | **US$38,1 ≈ 1,01 triệu ₫** | US$39,0 ≈ 1,03 triệu ₫ |
| Bình quân / 1 sản phẩm đăng | US$6,9 ≈ 183 nghìn ₫ | **US$5,4 ≈ 144 nghìn ₫** | US$5,6 ≈ 148 nghìn ₫ |

**Trả lời thẳng "ngân sách mỗi video":**
- **Video review dài 18 phút kèm 5 short: ~1,01 triệu ₫** (gói B, đã gồm mọi thuê bao + ngân sách test).
- **Chi phí phát sinh khi làm thêm 1 video dài** (còn credit): Kênh A **~403 nghìn ₫**, Kênh B **~281 nghìn ₫**.
- **Video flagship cấp Cao cấp:** ~1,14 triệu ₫ phát sinh.
- **Ngoài ngân sách tháng:** vốn nạp thử sàn cho Kênh B ~US$1.000 (thu hồi được); mua SPVL cho video flagship (tuỳ sản phẩm, có thể bán lại).

## 4. Lộ trình chi tiêu

| Thời gian | Gói | Chi phí |
|---|---|---|
| Tuần chuẩn bị 15–21/10: thiết lập + 2 video thử Kênh A | A | ~4,4 triệu ₫ |
| Từ 22/10: Kênh A 12 video/tháng; Kênh B chuẩn bị (test, kịch bản), **chỉ đăng khi có ý kiến luật sư** | B | ~20,2 triệu ₫/tháng |
| Sau khi Kênh A đạt YPP và KPI đạt | Cân nhắc C | ~41,4 triệu ₫/tháng |

**Tổng công cụ đến 31/01/2027: ~4,4 + 3 × 20,2 ≈ 65 triệu ₫** (chưa gồm nhân sự, vốn nạp thử sàn).

## 5. Doanh thu & điểm hoà vốn (sheet **DoanhThu**)

### Phễu affiliate — giả định thận trọng (thay bằng số thật sau 30 ngày)

| Mảng | Kênh | Tỷ trọng lượt xem | CTR link | Chuyển đổi/click | Hoa hồng TB | **Doanh thu / 1.000 lượt xem kênh** |
|---|---|---|---|---|---|---|
| SaaS & AI tool | A | 75% | 2% | 2% | US$40 | US$12,0 |
| SPVL (Amazon) | A | 25% | 3% | 5% | US$2,4 | US$0,9 |
| Forex (CPA) | B | 50% | 1,5% | 1% | US$400 | US$30,0 |
| Crypto (chia phí) | B | 50% | 1,5% | 2% | US$75 | US$11,3 |
| **Kênh A** | | | | | | **US$12,9** (+ RPM quảng cáo ~US$10 sau YPP) |
| **Kênh B** | | | | | | **US$41,3** (+ ~US$15 nếu được bật quảng cáo) |

### Hoà vốn (gói B, trước khi có quảng cáo YouTube)

| Kịch bản | Lượt xem / video dài / tháng để hoà vốn **công cụ** | … hoà vốn **cả lương** (15 triệu ₫, giả định) |
|---|---|---|
| Cả 2 kênh chạy (12 A + 8 B) | **~1.570** | **~2.740** |
| Chỉ Kênh A (20 video A, Kênh B không mở; cần nâng HeyGen lên bậc ~2.000 credit) | ~2.950 | ~5.140 |

Ví dụ thận trọng 3 tháng đầu — 2.000 lượt xem/video: doanh thu ~US$970/tháng (A ~US$310, B ~US$660) → **lãi ~US$208 nếu chỉ tính công cụ**, **lỗ ~9,5 triệu ₫/tháng nếu tính lương**.

**Lưu ý trung thực:**
- Tỷ lệ chuyển đổi affiliate là **giả định** — sai số có thể gấp đôi theo cả hai chiều. Sau 30 ngày thay bằng số thật từ dashboard affiliate.
- Forex CPA chỉ tính khi khách **đủ điều kiện** (nạp tiền + khối lượng giao dịch); crypto chia phí phụ thuộc thị trường.
- SaaS định kỳ **cộng dồn theo tháng** (chưa tính trong bảng → thận trọng).
- Chương trình affiliate có thời gian duyệt, ngưỡng thanh toán, chu kỳ trả tiền 30–60 ngày.
- Doanh thu Kênh B chỉ có khi Kênh B được phép mở.

## 6. Rủi ro chi phí & cách phòng

| Rủi ro | Phòng ngừa |
|---|---|
| HeyGen tính credit/phút cao hơn 20 | Ô ThongSo!B17; nếu 31 credit/phút → gói B cần ~1.750 credit/tháng (bậc ~2.000); hoặc giảm tỷ lệ người dẫn xuống 15% |
| Công cụ tăng giá / đổi chính sách | Bảng tính cập nhật trong 5 phút; mỗi bước có dự phòng |
| Gói Ultra chưa mở tại VN | AI Pro + Kling Pro + Seedance |
| Tốn tiền test sản phẩm | Ưu tiên bản dùng thử, tài khoản review do hãng cấp; hủy gói sau khi quay |
| Video 15+ phút tốn thời gian dựng | Template CapCut cho từng loại phần (tính năng, giá, so sánh) |

## 7. Phương án HeyGen Video Agent + trình dựng (chỉ Kênh A, Q9)

Sheet **ChiPhiVideo** mục E. Giả định: Video Agent tính credit trên **cả video 18 phút** × 1,3 lần xuất lại; không dùng Veo và ElevenLabs cho Kênh A. Credit/phút có 2 mức vì nguồn lệch nhau (20 theo eesel.ai, 40 theo diyai.io; HeyGen không công bố) ⚠️.

| Chỉ tiêu (gói B, 12 video Kênh A/tháng) | Hiện tại | HeyGen @20 | HeyGen @40 |
|---|---|---|---|
| Credit HeyGen / video | 94 | 468 | 936 |
| Chi phí biến đổi / video | US$15,19 (403 nghìn ₫) | US$22,93 (608 nghìn ₫) | US$45,86 (1,22 triệu ₫) |
| Gấp bao nhiêu lần hiện tại | 1,0x | 1,5x | 3,0x |
| Credit HeyGen cần / tháng | 1.123 | 5.616 | 11.232 |
| Tiền HeyGen / tháng | US$74 | ~US$275 | ~US$550 |
| **Tăng thêm / tháng** | — | **+5,3 triệu ₫** | **+12,6 triệu ₫** |
| Gói B / tháng (gồm 10% dự phòng phần tăng) | ~20,2 triệu ₫ | ~26,0 triệu ₫ | ~34,1 triệu ₫ |
| Nếu Kênh B không mở: cắt Flow Ultra → Pro, ElevenLabs Pro → Creator | — | −US$257 | −US$257 |
| **Chênh lệch ròng nếu Kênh B không mở** | — | **−1,5 triệu ₫** (rẻ hơn) | **+5,8 triệu ₫** |

Tiền HeyGen tính tuyến tính theo US$49/1.000 credit — gói Pro có nhiều bậc credit, chọn bậc gần nhất phía trên khi mua. Khi Kênh B không mở mà vẫn làm short native, short phải làm bằng HeyGen hoặc giảm số lượng vì AI Pro chỉ có ~2.500 credit Flow ⚠️.

**Kết luận:** chạy cả 2 kênh thì **chưa đáng đổi** (mỗi giờ tiết kiệm tốn 0,57–1,34 triệu ₫). Kênh B không mở và credit thật gần 20/phút thì **đáng đổi**. Quyết định sau video thử #2 (20/10) — cách thử ở [05 mục 7](05-bo-cong-cu.md#7-phương-án-thay-thế-heygen-video-agent--trình-dựng-q9--thử-ab-ngày-2010).

## 8. Dây chuyền tự động hằng ngày — bán tự động (Q10)

Sheet **ChiPhiVideo** mục F. Giữ nguyên các gói hiện tại; Veo vẫn tạo trong Flow (Flow không có API, Veo qua Gemini API đắt ~9,8 lần credit Ultra ở cấp Tiêu chuẩn).

| Chỉ tiêu (gói B, 20 video dài/tháng) | Giá trị |
|---|---|
| Claude API cho dây chuyền | US$3/video × 20 = US$60/tháng (trừ US$10 đã có) |
| Máy chạy | 0 (Claude Code theo lịch hoặc máy công ty) |
| HeyGen API chênh so với gói web | 0 (tạm tính) ⚠️ chưa xác minh giá API |
| **Tăng thêm / tháng (gồm 10% dự phòng)** | **+US$55 ≈ 1,46 triệu ₫** |
| Gói B khi có dây chuyền | ~US$816 ≈ **21,6 triệu ₫/tháng** |
| Giờ công tiết kiệm | ~41 giờ/tháng ≈ 3,97 triệu ₫ |
| Chi phí xây một lần | ~30 giờ ≈ 2,9 triệu ₫ → hoàn vốn ~1,2 tháng |

So với HeyGen Video Agent (mục 7): rẻ hơn ~3,7–8,7 lần tiền tăng thêm mỗi tháng (+1,46 so với +5,3–12,6 triệu ₫), mà tiết kiệm gấp ~2,7 lần thời gian (127 so với 47 phút/video). Chi tiết kỹ thuật: [11 mục 8](11-tich-hop-claude.md#8-dây-chuyền-tự-động-hằng-ngày--bán-tự-động-q10).
