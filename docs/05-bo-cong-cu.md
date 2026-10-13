# 05 — Bộ công cụ (giá tháng 10/2026)

> Giá là ảnh chụp từ trang giá chính thức và nguồn thứ cấp tháng 9–10/2026 — **xác nhận lại khi thanh toán**. Sửa giá trong sheet **CongCu** của [bảng tính](../ke-hoach/bang-tinh-ngan-sach-va-van-hanh.xlsx), mọi con số khác tự cập nhật.

## 1. Công cụ theo từng bước (gói B)

| Bước | Công cụ chính | Gói | Giá/tháng | Dự phòng | Vì sao |
|---|---|---|---|---|---|
| Não trung tâm: chọn sản phẩm, kịch bản, QC tuân thủ, SEO, phân tích | **Claude** (claude.ai, Claude Code, skill) | Max 5x | US$100 | Pro US$20 | Viết tiếng Anh tự nhiên, kiểm tuân thủ, có Projects + Skills; công ty đã có skill nghiên cứu affiliate SaaS/broker |
| Tự động cắt short | **Claude API** | Theo dùng | ~US$10 | — | Opus 5.5: US$4/US$20 mỗi 1 triệu token → vài cent/video |
| **Người dẫn AI trông như người thật** | **HeyGen** (Avatar IV, lồng từ file giọng) | Pro, bậc ~1.500 credit* | ~US$74* | Synthesia; Hedra | Phổ biến nhất cho người dẫn talking-head; video tới 30 phút; avatar riêng từ ảnh |
| Cảnh người thật do AI tạo | **Veo 3.1** trong Flow | Google AI Ultra 20x | US$199,99 | Kling (US$10) | Người thật chân thực nhất, có âm thanh, dọc 9:16 gốc |
| Ảnh, keyframe, thumbnail | **Nano Banana Pro** | Trong gói Google | 0 | — | Giữ nhân vật nhất quán, dùng ảnh sản phẩm thật làm tham chiếu |
| Giọng đọc (người dẫn + lời kể) | **ElevenLabs** | Pro (~600 phút/tháng) | US$99 | Creator US$22 | Giọng Mỹ tự nhiên; 1 giọng dùng cho cả HeyGen |
| **Quay màn hình sản phẩm** | **OBS Studio** / trình ghi CapCut | Miễn phí | 0 | Claude in Chrome thao tác web app | Dữ liệu thật |
| Dựng, phụ đề, zoom, bảng giá | **CapCut Pro** (desktop) | Pro | ~US$10 | DaVinci Resolve | Template, phụ đề tự động, quen thuộc |
| Nhạc | YouTube Audio Library + **Suno** | Suno Pro | US$10 | — | An toàn bản quyền; Pro mới có quyền thương mại |
| Cắt short | **`tools/cat_short.py`** + **OpusClip** | OpusClip Pro | US$29 | — | Tool Claude kiểm soát được (thêm dòng cảnh báo cho Kênh B) |
| **Dùng thử sản phẩm** | Gói SaaS/AI tool trả phí để test | — | US$150 | Tài khoản review do hãng cấp | Review phải dựa trên dùng thật |
| Hẹn giờ đăng | YouTube Studio, Meta Business Suite | Miễn phí | 0 | — | An toàn tài khoản |

\* HeyGen công bố Pro US$49/1.000 credit, có các bậc credit cao hơn; giá bậc ~1.500 credit là **ước tính tuyến tính** — xác nhận trên heygen.com/pricing. Avatar IV tốn ~20 credit/phút (nguồn thứ cấp ghi 16–31 tuỳ loại Look).

**Tổng gói B:** US$691,99 + 10% dự phòng = **~US$761/tháng ≈ 20,2 triệu ₫** (tỷ giá 26.500).

## 2. Người dẫn AI — cách làm đúng

1. **Tạo khuôn mặt hư cấu** bằng Nano Banana Pro (prompt trong [thư viện](../templates/thu-vien-prompt.md#3-tạo-người-dẫn-ai-1-lần)); kiểm tra **không giống người nổi tiếng/người thật** (tìm ảnh ngược bằng Google Lens).
2. Tạo **Photo Avatar / Avatar IV** trên HeyGen từ ảnh đó; lưu Avatar ID vào Bible.
3. Mỗi video: tải file `host_*.mp3` của ElevenLabs → HeyGen khớp khẩu hình → xuất 16:9 nền studio của kênh.
4. **Luôn công khai**: dòng chữ *"AI-generated presenter"* ở 30 giây đầu + bật nhãn "Altered or synthetic content" khi đăng + dòng trong mô tả.
5. **Không** dùng ảnh/giọng của người thật khi chưa có hợp đồng đồng ý bằng văn bản; **không** dùng người dẫn AI cho Kênh B.

## 3. Bảng credit Veo 3.1 & lý do chọn thuê bao

| Model | Credit/clip 8 giây — AI Pro | — AI Ultra | API (USD/giây, 1080p) |
|---|---|---|---|
| Veo 3.1 Lite | 10 | 5 | 0,08 |
| Veo 3.1 Fast | 20 | 10 | 0,12 |
| Veo 3.1 Quality | 100 | 100 | 0,40 |

Gói Google AI: Pro US$19,99 (1.000 credit + 50/ngày) · Ultra 5x US$99,99 (10.000) · **Ultra 20x US$199,99 (25.000)**. Một video dài cấp Tiêu chuẩn cần ~945 credit cho cảnh người AI ≈ **US$7,1** qua Ultra 20x (qua API ~US$70). Tính cả người dẫn, giọng, ảnh: **thuê bao rẻ hơn API ~5,7 lần** (Kênh B ~7,8 lần).

*Gói Ultra mới công bố ở Google I/O 2026 — kiểm tra có mở tại Việt Nam; nếu chưa: AI Pro + Kling Pro (US$37) + Seedance.*

## 4. Công cụ đã xem xét nhưng KHÔNG chọn

| Công cụ | Lý do |
|---|---|
| OpenAI Sora | Đã thông báo khai tử (24/03/2026) |
| Runway Gen-4.5 | ~12 credit/giây → đắt hơn Veo qua Flow cho cùng sản lượng |
| Tool "video từ chữ" dùng stock (InVideo, Pictory…) | Ra video rập khuôn — đúng loại YouTube không trả tiền |
| Deepfake/clone người thật không có hợp đồng | Vi phạm chính sách YouTube, luật quảng cáo, Luật Trí tuệ nhân tạo VN |
| Tài khoản chia sẻ/crack | Mất tài khoản, không quyền thương mại, rủi ro bảo mật |
| Gói miễn phí (HeyGen Free, ElevenLabs Free, Suno Free…) | Watermark và/hoặc không có quyền thương mại |

## 5. Quyền thương mại

| Công cụ | Điều kiện |
|---|---|
| Claude, Google AI, Veo, Nano Banana | Gói trả phí; video Veo có watermark ẩn SynthID |
| HeyGen | Gói trả phí; avatar từ ảnh **của mình/hư cấu**, không dùng ảnh người khác |
| ElevenLabs | Starter trở lên |
| Suno | Pro trở lên (bài tạo khi đang là thành viên Pro) |
| Kling | Gói trả phí — Kling cấp **quyền sử dụng**, đọc kỹ điều khoản |
| CapCut | Pro; **không dùng nhạc trong thư viện CapCut cho YouTube** |
| Logo/giao diện sản phẩm được review | Dùng để nhận diện & minh hoạ review (sử dụng hợp lý); không ngụ ý hãng tài trợ nếu không có |

## 6. Checklist mở tài khoản (ngày 1 sau review)

- [ ] 2 Gmail riêng (Kênh A, Kênh B), bật **xác minh 2 bước** bằng ứng dụng xác thực.
- [ ] 2 **YouTube Brand Account**, xác minh số điện thoại (video > 15 phút bắt buộc phải xác minh).
- [ ] Thẻ thanh toán quốc tế của công ty, 1 thẻ riêng cho chi phí AI.
- [ ] Gói A: Claude Pro, Google AI Pro, HeyGen Creator, ElevenLabs Creator, CapCut Pro; cài OBS.
- [ ] Trình quản lý mật khẩu dùng chung.
- [ ] Google Drive theo cấu trúc ở [04](04-quy-trinh-san-xuat.md#3-cấu-trúc-thư-mục--đặt-tên).
- [ ] Claude Project cho mỗi kênh + cài 3 skill của repo + bật skill `saas-affiliate-research`, `broker-affiliate-research`, `forex-broker` (xem [11](11-tich-hop-claude.md)).
- [ ] **Đăng ký chương trình affiliate** cho 10 sản phẩm đầu tiên (duyệt mất vài ngày–vài tuần); Amazon Associates (cần 3 đơn trong 180 ngày).
- [ ] Gửi **hồ sơ hỏi ý kiến luật sư** cho Kênh B (mẫu câu hỏi ở [09](09-chinh-sach-phap-ly-rui-ro.md#6-hồ-sơ-hỏi-ý-kiến-luật-sư-cho-kênh-b)).
- [ ] Trang trung gian/link rút gọn có thương hiệu trên website công ty (lọc quốc gia cho Kênh B).
