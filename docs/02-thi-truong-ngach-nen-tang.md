# 02 — Thị trường, ngách nội dung & vai trò từng nền tảng

## 1. Thị trường: Global, tiếng Anh

| Tiêu chí | Kênh tiếng Việt | **Kênh tiếng Anh (Global)** |
|---|---|---|
| RPM video dài (doanh thu thực nhận / 1.000 lượt xem) | ~US$0,2–1 (Dynamoi, 7/2026: RPM Việt Nam ~US$0,22) | **~US$4–12** tuỳ ngách (Giáo dục & Khoa học trung vị US$10,22 — AIR Media-Tech) |
| Quy mô khán giả | ~70 triệu người dùng | Hàng tỷ người dùng, nhiều nước có CPM cao (Mỹ, Anh, Canada, Úc, Bắc Âu) |
| Khả năng mở rộng | Hạn chế | Lồng tiếng sang Tây Ban Nha, Bồ Đào Nha, Hindi… bằng tính năng đa âm thanh của YouTube |
| Thách thức | — | Đội ngũ không phải người bản ngữ → **Claude làm biên tập viên tiếng Anh**, giọng ElevenLabs bản ngữ |

**Kết luận:** cùng một chi phí sản xuất, 1 lượt xem tiếng Anh từ khán giả Mỹ/Âu đáng giá gấp 10–30 lần lượt xem tiếng Việt.

**Hệ quả vận hành:**
- Giọng đọc: **tiếng Anh giọng Mỹ** (ElevenLabs), tốc độ ~150 từ/phút.
- Giờ đăng: theo giờ Mỹ/Âu → **hẹn giờ đăng 01:00–02:00 sáng giờ VN** (13:00–14:00 New York mùa đông). Không cần thức đêm — xem [07](07-nang-suat-lich-dang.md).
- Kiểm duyệt ngôn ngữ: mọi kịch bản qua **skill `qc-video`** của Claude (ngữ pháp, độ tự nhiên, nhạy cảm văn hoá).

## 2. Chọn ngách: tiêu chí & chấm điểm

Tiêu chí chọn ngách cho kênh **100% AI, không lộ mặt, khán giả toàn cầu**:
1. **RPM cao** (khán giả Mỹ/Âu, nhà quảng cáo trả nhiều).
2. **AI tạo ra giá trị mà quay thật không làm được** → đây là "giá trị gia tăng" giúp qua chính sách *inauthentic content*.
3. **Rủi ro chính sách thấp** (không đụng tài chính/y tế/pháp lý bằng nhân vật AI, không tin tức, không nội dung gây sốc).
4. **Nội dung "xanh mãi"** (evergreen) — video cũ vẫn kiếm view nhiều năm.
5. **Cắt short dễ** — có nhiều "khoảnh khắc ồ!" độc lập.
6. **Khối lượng kiểm chứng sự thật vừa phải.**

Thang điểm 1–5 (5 là tốt nhất):

| Ngách | RPM | Lợi thế AI | Rủi ro CS (5 = an toàn) | Evergreen | Dễ cắt short | Kiểm chứng (5 = nhẹ) | **Tổng** |
|---|---|---|---|---|---|---|---|
| **Lịch sử & Bí ẩn** (nền văn minh mất tích, sự kiện bí ẩn, "cuộc sống thời…") | 4 | **5** — tái hiện quá khứ không thể quay | 4 | 5 | 5 | 3 | **26** |
| Khoa học & Vũ trụ ("What if…", vũ trụ, cơ thể người) | **5** | 5 | 4 | 5 | 4 | 2 | 25 |
| Thần thoại & Truyền thuyết | 3 | 5 | **5** — rõ là tưởng tượng | 5 | 5 | 4 | **27** |
| Thiên nhiên & Động vật (phim tài liệu) | 3 | 4 | 3 — dễ bị coi "giả thật", cấm nội dung động vật đau khổ | 5 | 4 | 3 | 22 |
| Kỹ thuật "How it works" | 4 | 3 | 5 | 4 | 3 | 2 | 21 |

**Đề xuất:** Kênh 1 = **Lịch sử & Bí ẩn, có series phụ Thần thoại** (gộp 2 ngách điểm cao nhất, cùng phong cách hình ảnh, cùng khán giả). Kênh 2 (giai đoạn mở rộng) = **Khoa học & Vũ trụ** (RPM cao nhất nhưng cạnh tranh mạnh và phải kiểm chứng kỹ).

Ví dụ 10 chủ đề mở màn cho kênh 1:
1. The Lost City of Ubar — Atlantis of the Sands
2. What Daily Life Was Like in Ancient Rome (for a 10-year-old)
3. The Bronze Age Collapse: When Civilization Ended
4. Göbekli Tepe: The Temple Older Than Writing
5. The Mystery of the Sea Peoples
6. How Did the Egyptians Really Move the Stones?
7. The Library of Alexandria: What Was Really Lost
8. The Voynich Manuscript Explained
9. Norse Mythology: Ragnarök Told Like a Movie
10. The Real Story Behind the Trojan Horse

## 3. Ngách KHÔNG làm (rủi ro bị tắt kiếm tiền hoặc khoá kênh)

| Ngách | Lý do |
|---|---|
| Tài chính, y tế, pháp lý với **nhân vật/chuyên gia AI** | Bị cấm kiếm tiền từ 16/07/2026 ("AI persona" bàn chủ đề nhạy cảm) |
| Tin tức, chính trị, sự kiện nóng | Rủi ro sai lệch thông tin, nhãn cảnh báo, đòi hỏi tốc độ |
| Tổng hợp/re-up clip, phim, nhạc người khác | Vi phạm *reused content* + bản quyền |
| Truyện "Reddit", truyện đọc theo khuôn giống nhau | Điển hình của *generic/repetitive* — nhóm đầu tiên bị tắt kiếm tiền |
| Nội dung trẻ em (Made for Kids) | RPM thấp, tắt bình luận, tắt nhiều tính năng |
| "Giải cứu động vật", nội dung gây sốc, câu cảm xúc | Bị liệt vào *off-putting/distressing* — YouTube loại cả kênh khỏi YPP |
| Deepfake người nổi tiếng/người thật | Vi phạm chính sách, Luật Trí tuệ nhân tạo VN (Luật 134/2025/QH15) |

## 4. Vai trò từng nền tảng

| Nền tảng | Vai trò | Kiếm tiền trực tiếp với đội ngũ ở VN | Ghi chú |
|---|---|---|---|
| **YouTube (video dài)** | **Nguồn doanh thu chính** (quảng cáo, thành viên kênh) | Có — sau khi vào YPP; AdSense trả về tài khoản ngân hàng VN | RPM video dài gấp ~100 lần Shorts |
| **YouTube Shorts** | Kéo người đăng ký, đẩy người xem sang video dài (gắn "Related video") | Có — RPM ~US$0,03–0,10 | Phân phối toàn cầu theo nội dung/ngôn ngữ |
| **Facebook Reels** | Kéo traffic, xây thương hiệu | Kiểm tra quyền kiếm tiền trong Meta Business Suite | Đăng lại cùng file short |
| **Instagram Reels** | Kéo traffic, xây thương hiệu | Không có chương trình trả tiền cho VN | Reels > 3 phút không được đề xuất cho người mới |
| **TikTok** | Thử nghiệm 30 ngày | **Chưa** — Creator Rewards chỉ mở cho tài khoản đăng ký ở Mỹ, Anh, Đức, Pháp, Brazil, Nhật, Hàn (theo hỗ trợ TikTok, 8/2026) | Tài khoản đăng ký tại VN thường được phân phối ưu tiên cho người xem trong khu vực (kinh nghiệm phổ biến của cộng đồng creator). **Không dùng VPN/SIM giả để "lách" — vi phạm điều khoản.** |

> Nguyên tắc: **mọi short đều trỏ về YouTube**. Mục tiêu cuối là giờ xem video dài.

## 5. Mở rộng đa ngôn ngữ (giai đoạn 2, từ tháng thứ 3)

- YouTube đã mở **tự động lồng tiếng (auto-dubbing) cho mọi creator** (2/2026) và **đa track âm thanh** (creator tự tải bản lồng tiếng lên cùng 1 video).
- Cách làm: 1 video → thêm track Tây Ban Nha, Bồ Đào Nha, Hindi, Indonesia, Đức, Pháp. **Không phải đăng lại video** → không bị coi là trùng lặp, lượt xem dồn về 1 video.
- Thứ tự: dùng **auto-dubbing miễn phí** của YouTube trước → video nào tốt mới làm bản lồng tiếng chất lượng cao bằng ElevenLabs.
