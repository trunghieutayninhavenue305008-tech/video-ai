# 03 — Định dạng, độ dài & mô hình "làm dài trước, cắt short sau"

## 1. Độ dài tối thiểu / tối đa

### Giới hạn của nền tảng (tham chiếu)

| Nền tảng | Định dạng | Giới hạn kỹ thuật |
|---|---|---|
| YouTube | Video dài | Tới 12 giờ (tài khoản đã xác minh). **Từ 8 phút trở lên mới chèn được quảng cáo giữa video (mid-roll).** |
| YouTube Shorts | Dọc 9:16 | Tối đa **3 phút** (từ 15/10/2024) |
| TikTok | Dọc | Quay trong app tới 10 phút, tải lên dài hơn |
| Instagram Reels | Dọc | Tới 20 phút, nhưng **trên 3 phút không được đề xuất cho người mới** |
| Facebook Reels | Dọc | Phổ biến **≤ 90 giây** (cần kiểm tra lại trong Meta Business Suite) |

### Quy chuẩn của kênh (đề xuất)

| Loại | Tối thiểu | **Chuẩn** | Tối đa | Lý do |
|---|---|---|---|---|
| **Video dài 16:9** | **8 phút** | **10–12 phút** | 15 phút (giai đoạn 1), 20 phút (từ tháng 3) | ≥ 8 phút để có mid-roll; > 15 phút chất lượng AI khó giữ đều, chi phí tăng tuyến tính |
| **Short cắt từ video dài** | 20 giây | **30–50 giây** | **90 giây** | ≤ 90 giây thì 1 file đăng được cả 4 nền tảng |
| **Short native** (làm riêng dạng dọc) | 15 giây | **30–45 giây** | 60 giây | Ngắn, 1 ý, vòng lặp (loop) tốt |

> Mẹo: short càng ngắn thì tỷ lệ xem hết càng cao. Một short 35 giây xem hết 90% tốt hơn short 70 giây xem hết 40%.

## 2. Video dài hay short? — Làm cả hai, theo tỷ lệ cố định

| | Video dài | Short |
|---|---|---|
| Vai trò | **Kiếm tiền** (RPM ~US$4–12) + giờ xem cho YPP | **Kéo người xem mới** + người đăng ký (RPM ~US$0,03–0,10) |
| Đóng góp cho YPP | Giờ xem (4.000 giờ) | Không tính giờ xem; tính đường riêng 10 triệu view/90 ngày |
| Chi phí | ~US$8,7 biến đổi/video (cấp Tiêu chuẩn) | Short cắt gần như 0; short native ~US$1 |

**Tỷ lệ chuẩn: 1 video dài → 5 short cắt + 1 short native.** Gói B (20 video dài/tháng) cho ra **120 short/tháng ≈ 4 short/ngày**.

## 3. Mô hình "kim tự tháp nội dung": dài trước → cắt short

```
                 ┌──────────────────────────┐
                 │  1 VIDEO DÀI 10–12 phút  │  ← kiếm tiền, giờ xem
                 └────────────┬─────────────┘
           ┌──────────┬───────┼───────┬──────────┐
         Short 1   Short 2  Short 3  Short 4   Short 5   ← cắt từ 5 chương mạnh nhất
           └──────────┴───────┴───────┴──────────┘
                              +
                     1 short native 9:16         ← "teaser" làm riêng, chất lượng cao nhất
                              ↓
        Đăng YouTube Shorts → đăng lại Reels (FB/IG), TikTok
        Mọi short gắn "Related video" trỏ về video dài
```

### Điều kiện để cắt short **không phải sửa gì**: kịch bản viết dạng MODULE

Đây là chìa khoá. Nếu viết kịch bản dài như một bài văn liền mạch thì cắt ra short sẽ cụt đầu cụt đuôi, phải sửa tay rất mất thời gian. Vì vậy **skill `kich-ban-video` của Claude luôn viết theo khung sau**:

| Phần | Thời lượng | Nội dung | Có thành short? |
|---|---|---|---|
| **Cold open (hook)** | 0:00–0:30 | Câu hỏi/khoảnh khắc gây tò mò nhất, hình ảnh mạnh nhất | Có thể |
| Lời hứa | 0:30–0:50 | "Trong video này bạn sẽ biết…" | Không |
| **Chương 1…6–8** | 60–90 giây/chương | Mỗi chương là **1 câu chuyện nhỏ độc lập**: *câu mở gây tò mò → nội dung → kết có "cú twist"* | **Có — mỗi chương là 1 short tiềm năng** |
| Cao trào / lời giải | 60–90 giây | Trả lời câu hỏi ở hook | Có thể |
| Kết + kêu gọi | 15–20 giây | Gợi ý video tiếp theo | Không |

**Quy tắc viết chương (để cắt short sạch):**
1. Câu đầu tiên của chương **đứng một mình vẫn hiểu** — không bắt đầu bằng "And then…", "As we saw…".
2. Không nhắc "như đã nói ở trên" trong chương.
3. Câu cuối chương là "cú chốt" (twist/sự thật bất ngờ) → short kết thúc có hậu.
4. Mỗi chương có 1 hình ảnh "đinh" đặt ở giây đầu tiên.

## 4. Khung hình: làm 16:9 nhưng phải cắt được sang 9:16

Video dài là 16:9 (ngang). Khi cắt sang 9:16 (dọc), chỉ giữ được **~32% chiều ngang ở giữa**. Ba cách xử lý, theo thứ tự ưu tiên:

| Cách | Khi nào dùng | Chi phí |
|---|---|---|
| **1. Bố cục "an toàn trung tâm" ngay từ prompt** — mọi cảnh có chủ thể ở giữa khung (prompt luôn có `subject centered, centered composition`) | Mặc định cho mọi cảnh | 0 — chỉ cắt giữa |
| **2. Nền mờ** — video 16:9 đặt giữa, nền là chính video đó phóng to + làm mờ, phụ đề to ở trên/dưới | Cảnh rộng, nhiều chủ thể | 0 — tool `cat_short.py` chế độ `blur` |
| **3. Tạo lại cảnh "đinh" bằng 9:16 gốc** (Veo 3.1 hỗ trợ dọc gốc) | 1–2 cảnh mở đầu short quan trọng nhất | ~20–40 credit/cảnh |

## 5. Thông số xuất file chuẩn (không phải nghĩ lại mỗi lần)

| | Video dài | Short |
|---|---|---|
| Khung hình | 1920×1080, 16:9 | 1080×1920, 9:16 |
| Khung hình/giây | 24 fps (điện ảnh) hoặc 30 fps | 30 fps |
| Codec | H.264, MP4 | H.264, MP4 |
| Âm lượng | -14 LUFS, đỉnh ≤ -1 dBTP | -14 LUFS |
| Nhạc nền dưới giọng | thấp hơn giọng ~18–20 dB | thấp hơn giọng ~15 dB |
| Phụ đề | Tệp SRT tải riêng lên YouTube (không cần cháy vào hình) | **Cháy vào hình**, chữ to, đặt ở 1/3 dưới, tránh vùng nút bấm bên phải |
| Vùng an toàn short | — | Không đặt chữ ở 15% trên cùng, 20% dưới cùng và 15% bên phải (che bởi nút/caption) |

Các thông số này được lưu sẵn thành **preset xuất** trong CapCut và trong tool `cat_short.py` → không ai phải nhớ.
