# CHECKLIST 2 CỔNG DUYỆT

> Người duyệt **chỉ đánh dấu Đạt/Không đạt và ghi mã lỗi** (ví dụ `K3`, `V6`) vào sheet **TheoDoi**, cột "Lỗi phát hiện ở Cổng 2". Không ngồi sửa tay. Mã `L1–L20` tham chiếu bảng 20 lỗi ở [docs/08](../docs/08-chong-loi-lat-vat.md#3-top-20-lỗi-lặt-vặt-hay-gặp-khi-làm-video-ai--cách-chặn-từ-gốc).

## Cổng 1 — Kịch bản

*Trước khi người duyệt: chạy skill `qc-video` với kịch bản + shot list. Người duyệt đọc báo cáo của Claude rồi kiểm các mục dưới đây (10 phút).*

| Mã | Kiểm tra | Đạt |
|---|---|---|
| K1 | Hook 30 giây đầu có câu hỏi/khoảnh khắc gây tò mò rõ ràng | ☐ |
| K2 | Có 6–8 chương; **mỗi chương đứng độc lập** (câu đầu không bắt đầu bằng "And/So/As we saw") | ☐ |
| K3 | Mỗi chương kết bằng twist/sự thật bất ngờ | ☐ |
| K4 | Mọi con số, năm, tên riêng có nguồn trong brief (L15) | ☐ |
| K5 | Điều chưa chắc chắn dùng câu thận trọng ("historians believe…") | ☐ |
| K6 | Không có từ cấm trong Bible (L16) | ☐ |
| K7 | Bản đọc đã viết số thành chữ, đã chèn phiên âm tên riêng (L4, L5) | ☐ |
| K8 | Độ dài 1.400–1.800 từ | ☐ |
| K9 | Shot list đủ cảnh, mỗi cảnh có prompt ảnh + prompt video + loại model; prompt có chuỗi phong cách Bible và `no text` (L1) | ☐ |
| K10 | Không có cận cảnh tay/khuôn mặt nói chuyện trong shot list (L2) | ☐ |
| K11 | Không đụng vùng cấm: tài chính/y tế/pháp lý, tin tức, người thật, thao túng cảm xúc | ☐ |
| K12 | Đã đánh dấu 5 chương làm short | ☐ |

**Kết luận Cổng 1:** ☐ Đạt → đóng băng kịch bản · ☐ Không đạt → trả lại Bước 2 kèm mã lỗi

## Cổng 2 — Video hoàn chỉnh

*Xem tua 1,5–2x toàn bộ video + xem kỹ 30 giây đầu ở tốc độ thường (10 phút).*

### Hình & âm
| Mã | Kiểm tra | Đạt |
|---|---|---|
| V1 | 30 giây đầu: hình mạnh, không chữ giới thiệu dài dòng | ☐ |
| V2 | Không có chữ lỗi do AI vẽ (L1) | ☐ |
| V3 | Không có tay/chân/mặt biến dạng nhìn thấy rõ (L2) | ☐ |
| V4 | Nhân vật lặp lại nhất quán giữa các cảnh (L3) | ☐ |
| V5 | Không có khung đen, khoảng trống, giật hình (L10) | ☐ |
| V6 | Phụ đề đúng chính tả, ngắt dòng gọn, khớp giọng (L6) | ☐ |
| V7 | Giọng đọc đúng tên riêng, số, không vấp (L4, L5) | ☐ |
| V8 | Nhạc không át giọng; không còn âm thanh lạ từ clip Veo (L8, L9) | ☐ |
| V9 | Âm lượng chuẩn -14 LUFS (preset) (L7) | ☐ |
| V10 | Logo/intro/end screen đúng template | ☐ |

### Xuất bản
| Mã | Kiểm tra | Đạt |
|---|---|---|
| P1 | Tiêu đề ≤ 60 ký tự, không sai chính tả (L13) | ☐ |
| P2 | 3 thumbnail, đọc được ở 160 px, chữ ≤ 4 từ, không lỗi chính tả (L14) | ☐ |
| P3 | Mô tả có chapter, nguồn tham khảo, dòng công khai AI, link video liên quan (L19) | ☐ |
| P4 | **Đã bật "Altered or synthetic content" nếu có cảnh tái hiện chân thực** (L17) | ☐ |
| P5 | Phụ đề SRT đã tải lên; ngôn ngữ video = English | ☐ |
| P6 | Nhạc thuộc YouTube Audio Library hoặc Suno Pro — không nhạc CapCut (L18) | ☐ |
| P7 | Hẹn giờ đúng khung (02:00 giờ VN), playlist đúng series | ☐ |

### Short (mỗi short xem hết 1 lần)
| Mã | Kiểm tra | Đạt |
|---|---|---|
| S1 | 1080×1920, 20–90 giây (L11) | ☐ |
| S2 | Câu đầu hiểu được khi đứng một mình; câu cuối là twist | ☐ |
| S3 | Phụ đề không bị nút bấm che (vùng an toàn) (L12) | ☐ |
| S4 | Chủ thể không bị cắt mất khi chuyển 9:16 (nếu mất → dùng chế độ `blur`) | ☐ |
| S5 | Tiêu đề, hashtag đúng từng nền tảng (từ `shorts.csv`) | ☐ |
| S6 | Gắn "Related video" trỏ về video dài trên YouTube | ☐ |

**Kết luận Cổng 2:** ☐ Đạt → hẹn giờ · ☐ Không đạt → ghi mã lỗi vào TheoDoi, sửa, **và ghi nguyên nhân gốc** (Bible/skill/template nào phải sửa).
