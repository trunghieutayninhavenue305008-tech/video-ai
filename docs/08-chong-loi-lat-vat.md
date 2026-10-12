# 08 — Hệ thống chống lỗi lặt vặt ("làm đúng ngay từ đầu")

> Yêu cầu: **hạn chế tối đa việc sửa những lỗi nhỏ nhặt.** Cách làm: không "sửa giỏi" mà **chặn lỗi từ gốc** — mỗi lỗi chỉ được phép xảy ra 1 lần, lần thứ 2 phải được chặn bằng template, Bible hoặc checklist.

## 1. Năm lớp phòng thủ

| Lớp | Công cụ | Chặn loại lỗi nào |
|---|---|---|
| **1. Bible kênh** ([mẫu](../templates/kenh-bible.md)) | Tài liệu duy nhất về giọng văn, phong cách hình, font, màu, từ cấm, phát âm | Lệch phong cách giữa các video, mỗi người làm một kiểu |
| **2. Skill Claude** ([.claude/skills](../.claude/skills/)) | `kich-ban-video`, `seo-xuat-ban`, `qc-video` — đầu ra luôn đúng 1 khuôn | Kịch bản thiếu phần, prompt thiếu thông số, tiêu đề quá dài |
| **3. Template & preset** | Template CapCut (phụ đề, intro, chuyển cảnh), preset xuất file, thư viện prompt ([mẫu](../templates/thu-vien-prompt.md)) | Sai khung hình, sai font, âm lượng không đều, quên logo |
| **4. Hai cổng duyệt** ([checklist](../templates/checklist-qc.md)) | Cổng 1 (kịch bản) + Cổng 2 (video) | Lỗi lọt qua 3 lớp trên |
| **5. Nhật ký lỗi → sửa gốc** | Cột "Lỗi phát hiện" + "Nguyên nhân gốc" trong sheet **TheoDoi** | Lỗi lặp lại |

**Quy tắc vàng:** lỗi phát hiện ở Cổng 2 → ghi vào TheoDoi → **cuối tuần cập nhật Bible/skill/template** để lỗi đó không thể xảy ra lần nữa. Mục tiêu KPI: **< 10% video phải sửa sau Cổng 2** (tuần 1 có thể 30%, giảm dần).

## 2. Vì sao Cổng 1 (kịch bản) là quan trọng nhất

| Sửa ở đâu | Chi phí sửa 1 lỗi |
|---|---|
| Trong kịch bản (Cổng 1) | ~10 giây, 0 credit |
| Sau khi đã tạo giọng | ~3 phút, tạo lại câu thoại |
| Sau khi đã tạo hình/clip | ~15 phút, tốn credit |
| Sau khi đã dựng xong | ~30 phút: giọng + hình + căn lại timeline + phụ đề |
| Sau khi đã đăng | Không sửa được video — phải gỡ và đăng lại, mất lượt xem |

→ **Mọi con số, tên riêng, năm tháng, câu chữ phải "đóng băng" ở Cổng 1.** Sau Cổng 1 không ai được sửa kịch bản trừ khi quay lại Cổng 1.

## 3. Top 20 lỗi lặt vặt hay gặp khi làm video AI & cách chặn từ gốc

| # | Lỗi | Phát hiện ở | Cách chặn từ gốc (không phải sửa tay) |
|---|---|---|---|
| 1 | AI vẽ chữ sai chính tả trong ảnh/video | Cổng 2 | Prompt luôn có `no text, no letters, no watermark`; mọi chữ thêm ở CapCut |
| 2 | Ngón tay/thân thể biến dạng | Cổng 2 | Shot list tránh cận cảnh tay; dùng góc rộng/trung; tạo 2–3 bản chọn bản tốt |
| 3 | Nhân vật đổi mặt giữa các cảnh | Cổng 2 | Ảnh tham chiếu cố định trong Bible + "Ingredients to Video" của Veo 3.1 |
| 4 | Giọng AI đọc sai tên riêng (Göbekli Tepe, Ubar…) | Bước 3 | **Từ điển phát âm** trong Bible; skill viết sẵn phiên âm trong ngoặc cho giọng đọc |
| 5 | Giọng đọc sai số/năm ("1200 BC" đọc thành "one thousand two hundred B C") | Bước 3 | Skill tự viết số thành chữ trong bản đọc ("twelve hundred B.C.") |
| 6 | Phụ đề sai chính tả, ngắt dòng xấu | Cổng 2 | Phụ đề lấy **từ kịch bản đã duyệt**, không nhận dạng giọng nói; preset tối đa 42 ký tự/dòng, 2 dòng |
| 7 | Âm lượng giữa các video chênh nhau | Cổng 2 | Preset chuẩn hoá -14 LUFS khi xuất |
| 8 | Nhạc nền át giọng | Cổng 2 | Bật tự động hạ nhạc (ducking) trong template CapCut |
| 9 | Âm thanh gốc của Veo lạc lõng (tiếng nói lảm nhảm, nhạc lạ) | Bước 6 | Quy tắc: tắt tiếng clip Veo, chỉ giữ tiếng môi trường đã chọn |
| 10 | Khung đen / khoảng trống trên timeline | Cổng 2 | CapCut: bật "magnetic timeline"; xem tua nhanh 2x toàn bộ trước khi xuất |
| 11 | Sai khung hình (short bị viền đen, video dài bị méo) | Bước 8 | Preset xuất cố định; tool `cat_short.py` luôn xuất đúng 1080×1920 |
| 12 | Chữ trên short bị nút bấm che | Bước 8 | Vùng an toàn trong template short; tool cháy phụ đề ở 1/3 dưới, chừa lề phải |
| 13 | Tiêu đề quá dài bị cắt cụt | Bước 7 | Skill `seo-xuat-ban` giới hạn ≤ 60 ký tự, từ khoá chính ở 40 ký tự đầu |
| 14 | Thumbnail chữ sai/khó đọc trên điện thoại | Bước 7 | Tối đa 4 từ, font Bible, kiểm tra ở kích thước 160 px |
| 15 | Sai sự thật lịch sử/khoa học | Cổng 1 | Skill bắt buộc mỗi khẳng định có nguồn; `qc-video` đối chiếu nguồn; câu không chắc chắn phải dùng "historians believe…" |
| 16 | Văn phong "AI" sáo rỗng ("delve", "tapestry", "in today's fast-paced world") | Cổng 1 | Danh sách từ cấm trong Bible + skill tự tránh |
| 17 | Quên bật nhãn "nội dung đã chỉnh sửa/tổng hợp" khi cần | Cổng 2 | Ô bắt buộc trong checklist Cổng 2 + quy tắc rõ ràng ở [09](09-chinh-sach-phap-ly-rui-ro.md) |
| 18 | Nhạc bị Content ID claim | Sau đăng | Chỉ dùng YouTube Audio Library hoặc nhạc Suno tạo khi đang là thành viên Pro; **không dùng nhạc trong CapCut** |
| 19 | Mô tả thiếu chapter/thiếu link video liên quan | Bước 7 | Skill xuất mô tả đúng khuôn có sẵn chapter từ shot list |
| 20 | File để lộn xộn, mất bản gốc | Mọi bước | Cấu trúc thư mục & quy tắc đặt tên cố định ([04](04-quy-trinh-san-xuat.md#3-cấu-trúc-thư-mục--đặt-tên-google-drive)) |

## 4. "Định nghĩa hoàn thành" cho từng bước

Một bước chỉ được coi là xong khi đạt đủ điều kiện dưới đây — không "xong 90%" rồi để bước sau sửa.

| Bước | Hoàn thành khi |
|---|---|
| Kịch bản | Qua Cổng 1; có shot list đủ prompt; có từ điển phát âm; có danh sách 5 chương làm short |
| Giọng đọc | Nghe hết 1 lượt, không sai phát âm tên riêng, khoảng lặng giữa chương 0,5–0,8 giây |
| Ảnh | Đủ ảnh theo shot list, đúng tỷ lệ, không chữ, nhân vật khớp ảnh tham chiếu |
| Clip | Mỗi cảnh trong shot list có 1 clip được chọn, đặt tên `Sxxx_final.mp4` |
| Dựng | Xuất 1080p, -14 LUFS, phụ đề SRT riêng, không khung đen |
| SEO | Tiêu đề ≤ 60 ký tự, mô tả có chapter + nguồn tham khảo, 3 thumbnail |
| Short | 1080×1920, 20–90 giây, câu đầu đứng độc lập, có tiêu đề + hashtag từng nền tảng |

## 5. Ai sửa gì — tránh "sửa vặt" kéo dài

- **Người duyệt chỉ đánh dấu Đạt / Không đạt + ghi lỗi theo mã** trong checklist (ví dụ "L6 — phụ đề ngắt dòng"), không ngồi sửa tay từng chỗ.
- Lỗi nào lặp **≥ 2 lần trong tuần** → bắt buộc sửa gốc (Bible / skill / template) trong buổi tổng kết thứ Sáu.
- Lỗi "khẩu vị" (thích màu này hơn màu kia) **không phải lỗi** — gom lại, quyết 1 lần, ghi vào Bible.
