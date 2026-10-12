# 05 — Bộ công cụ (giá tháng 10/2026)

> Giá là ảnh chụp từ trang giá chính thức và nguồn thứ cấp tháng 9–10/2026 — **xác nhận lại khi thanh toán**. Sửa giá trong sheet **CongCu** của [bảng tính](../ke-hoach/bang-tinh-ngan-sach-va-van-hanh.xlsx), mọi con số khác tự cập nhật.

## 1. Bộ công cụ theo từng bước

| Bước | Công cụ chính | Gói đề xuất (gói B) | Giá/tháng | Dự phòng | Vì sao chọn |
|---|---|---|---|---|---|
| Não trung tâm: nghiên cứu, kịch bản, prompt, SEO, QC tiếng Anh, phân tích | **Claude** (claude.ai + Claude Code) | Max 5x | US$100 | Pro US$20 (gói A) | Viết tiếng Anh tự nhiên, suy luận tốt, có Projects + Skills để "khoá" phong cách kênh, Claude Code chạy tự động hoá |
| Tự động hoá (cắt short hàng loạt) | **Claude API** | Trả theo dùng | ~US$10 | — | Opus 5.5: US$4/US$20 mỗi 1 triệu token vào/ra → ~vài cent/video |
| Tạo video | **Google Veo 3.1 trong Flow** | Google AI Ultra (20x) | US$199,99 | Google AI Pro US$19,99 (gói A) | Chất lượng & bám prompt tốt nhất, có âm thanh, dọc 9:16 gốc, giữ nhân vật bằng "Ingredients"; **thuê bao rẻ hơn API ~14 lần** |
| Tạo ảnh / nhân vật / thumbnail | **Nano Banana Pro** (Gemini 3 Pro Image) | Đã gồm trong Google AI | 0 | Midjourney | Giữ nhân vật nhất quán, sửa ảnh bằng lời, nằm sẵn trong Flow |
| Video dự phòng | **Kling AI** (3.0) | Standard | US$10 | Seedance 2.0 (Dreamina), Hailuo 02 | Clip dài hơn, điều khiển chuyển động; rẻ theo giây |
| Giọng đọc & lồng tiếng | **ElevenLabs** | Pro (~600 phút/tháng) | US$99 | Creator US$22 (gói A) | Giọng tiếng Anh tự nhiên nhất; có lồng tiếng đa ngôn ngữ |
| Dựng & phụ đề | **CapCut Pro** (desktop) | Pro | ~US$10 (≈220–290 nghìn ₫) | DaVinci Resolve (miễn phí) | Phụ đề tự động, template, auto-reframe, quen thuộc với người Việt |
| Nhạc | **YouTube Audio Library** + **Suno** | Suno Pro | US$10 | — | Thư viện YouTube an toàn bản quyền; Suno tạo nhạc chủ đề riêng (Pro mới có quyền thương mại) |
| Cắt short | **Tool `cat_short.py`** (Claude + ffmpeg) + **OpusClip** | OpusClip Pro | US$29 | — | Tool Claude miễn phí, kiểm soát được; OpusClip tiện, có điểm viral + hẹn giờ đăng |
| Hẹn giờ đăng | YouTube Studio, Meta Business Suite, TikTok Studio | Miễn phí | 0 | OpusClip scheduler | Công cụ gốc của nền tảng, an toàn tài khoản |
| SEO / ý tưởng | vidIQ (bản miễn phí) | Miễn phí | 0 | — | Xem lượng tìm kiếm, đối thủ |

**Tổng gói B:** US$467,99 + 10% dự phòng = **~US$515/tháng ≈ 13,6 triệu ₫** (tỷ giá 26.500).

## 2. Những công cụ đã xem xét nhưng KHÔNG chọn

| Công cụ | Lý do |
|---|---|
| **OpenAI Sora** | OpenAI thông báo **khai tử Sora (app & API) ngày 24/03/2026**. Không xây quy trình trên công cụ đang đóng cửa. |
| Runway (Gen-4.5) | Chất lượng tốt nhưng ~12 credit/giây → đắt hơn Veo qua Flow nhiều lần cho cùng sản lượng. Giữ làm phương án nếu cần công cụ chỉnh sửa video chuyên sâu. |
| HeyGen, Synthesia (người dẫn AI) | Kênh không dùng người dẫn; nhân vật AI "nói chuyện" dễ lỗi khẩu hình và vướng quy định AI persona. |
| InVideo AI, Pictory (tự làm video từ chữ) | Ra video rập khuôn, dùng stock footage chung → đúng kiểu nội dung YouTube **không trả tiền**. |
| Giọng Việt (Vbee, FPT.AI) | Không cần — thị trường là tiếng Anh. |
| Tài khoản "chia sẻ"/crack (CapCut Pro 25 nghìn ₫…) | Rủi ro mất tài khoản giữa chừng, không có quyền thương mại, rủi ro bảo mật. **Chỉ mua chính hãng.** |
| Gói miễn phí của mọi công cụ | Có watermark và/hoặc **không có quyền thương mại** (ElevenLabs Free, Suno Free, Kling Free). Chỉ dùng để thử. |

## 3. Bảng tính credit Veo 3.1 (để hiểu vì sao chọn thuê bao)

| Model | Credit/clip 8 giây — Google AI Pro | Credit/clip — Google AI Ultra | Giá API (USD/giây, 1080p) |
|---|---|---|---|
| Veo 3.1 Lite | 10 | 5 | 0,08 |
| Veo 3.1 Fast | 20 | 10 | 0,12 |
| Veo 3.1 Quality | 100 | 100 | 0,40 |

| Gói Google AI | Giá | Credit Flow/tháng | Credit/ngày (không cộng dồn) |
|---|---|---|---|
| AI Pro | US$19,99 | 1.000 | 50 |
| AI Ultra 5x | US$99,99 | 10.000 | 50 |
| **AI Ultra 20x** | **US$199,99** | **25.000** | 50 |

→ Với Ultra 20x, 1 clip Fast 8 giây ≈ 10 credit ≈ **US$0,075**; qua API cùng clip đó là **US$0,96**. Một video dài cấp Tiêu chuẩn cần ~900 credit ≈ **US$6,8** (qua API: ~US$94).

*Nguồn: diyai.io (cập nhật 20/09/2026), Gemini API pricing. Gói Ultra mới (5x/20x) công bố tại Google I/O 2026 — **kiểm tra gói có mở tại Việt Nam khi đăng ký**; nếu chưa có: dùng AI Pro + nâng Kling lên Pro (US$37) + Seedance.*

## 4. Quyền thương mại — điều kiện bắt buộc

| Công cụ | Gói tối thiểu được dùng thương mại | Ghi chú |
|---|---|---|
| Claude | Mọi gói trả phí | Đầu ra thuộc người dùng theo điều khoản |
| Google AI / Veo / Nano Banana | Gói trả phí | Video Veo có watermark ẩn SynthID (không ảnh hưởng hiển thị) |
| ElevenLabs | **Starter trở lên** | Free không có quyền thương mại |
| Suno | **Pro trở lên** | Bài tạo khi đang là thành viên Pro mới có quyền thương mại; bài tạo ở gói Free thuộc Suno |
| Kling | Gói trả phí | Đọc kỹ điều khoản: Kling cấp **quyền sử dụng**, không phải quyền sở hữu toàn phần |
| CapCut | Pro | Một số template/nhạc trong CapCut chỉ dùng cá nhân → **không dùng nhạc CapCut cho YouTube** |

## 5. Checklist mở tài khoản (ngày 1 sau review)

- [ ] 1 Gmail riêng cho kênh (không dùng mail cá nhân), bật **xác minh 2 bước** bằng ứng dụng xác thực.
- [ ] Tạo **YouTube Brand Account** (cho phép thêm người quản lý sau này), xác minh số điện thoại để mở video > 15 phút, thumbnail tuỳ chỉnh.
- [ ] Thẻ thanh toán quốc tế của công ty (Visa/Mastercard) — 1 thẻ riêng cho chi phí AI để dễ đối soát.
- [ ] Đăng ký theo gói A: Claude Pro, Google AI Pro, ElevenLabs Creator, CapCut Pro.
- [ ] Trình quản lý mật khẩu dùng chung (Bitwarden/1Password) — không gửi mật khẩu qua chat.
- [ ] Tạo Google Drive theo cấu trúc thư mục ở [04](04-quy-trinh-san-xuat.md#3-cấu-trúc-thư-mục--đặt-tên-google-drive).
- [ ] Tạo Claude Project "Kênh 1" + tải Bible + cài 3 skill (xem [11](11-tich-hop-claude.md)).
- [ ] AdSense: tạo sẵn khi kênh gần đủ điều kiện (thông tin công ty, tài khoản ngân hàng nhận USD).
