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
| Tool "video từ chữ" dùng stock (InVideo, Pictory…) | Ra video rập khuôn — đúng loại YouTube không trả tiền (HeyGen Video Agent cũng dùng cảnh kho → chỉ **thử nghiệm**, xem mục 7) |
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

## 7. Phương án thay thế: HeyGen Video Agent + trình dựng (Q9 — thử A/B ngày 20/10)

**Là gì:** đưa kịch bản Claude viết vào **Video Agent** → HeyGen tự tạo bản nháp gồm người dẫn, giọng, B-roll và phụ đề → mở **trình dựng (AI Studio)** của HeyGen để chèn quay màn hình, bảng giá, sửa cảnh → xuất. Một công cụ thay cho bước 5–8 (ElevenLabs → HeyGen → Veo → CapCut).

**Không thay được:** bước 1–4 (nghiên cứu, **test & quay màn hình thật**, kịch bản, Cổng 1) và bước 9–10 (thumbnail/SEO, Cổng 2). FTC vẫn bắt buộc review dựa trên trải nghiệm thật.

| Thông tin | Giá trị | Nguồn |
|---|---|---|
| Credit / phút Video Agent | **20** (eesel.ai) hoặc **40** (diyai.io, 04/09/2026); tuỳ chọn Seedance 120 | ⚠️ HeyGen không công bố số theo phút; Help Center chỉ xếp Video Agent vào nhóm "tốn nhiều credit" |
| Phần bị tính credit | ⚠️ Chưa rõ đoạn quay màn hình tải lên có bị tính không → bảng tính giả định **tính cả video** | — |
| Sửa rồi xuất lại | Tốn credit lần nữa → hệ số **1,3** | diyai.io; ô ThongSo!B53 |
| Video tối đa | 30 phút (Creator/Pro) | heygen.com/pricing |
| Credit thừa | Gói tháng chuyển sang được **1 kỳ** | HeyGen Help Center |
| Gói có Video Agent | Help Center ghi rõ ở Pro; Creator chưa ghi rõ ⚠️ | HeyGen Help Center |

**Chi phí & hiệu suất** (sheet **ChiPhiVideo** mục E, **NangSuat** mục so sánh — Kênh A, gói B, 12 video/tháng):

| | Hiện tại | HeyGen @20 credit/phút | HeyGen @40 credit/phút |
|---|---|---|---|
| Credit HeyGen / video | 94 | 468 | 936 |
| Chi phí biến đổi / video 18 phút | US$15,19 ≈ 403 nghìn ₫ | US$22,93 ≈ 608 nghìn ₫ | US$45,86 ≈ 1,22 triệu ₫ |
| Tiền HeyGen / tháng | US$74 | ~US$275 | ~US$550 |
| Gói B / tháng | ~20,2 triệu ₫ | ~26,0 triệu ₫ | ~34,1 triệu ₫ |
| Phút / video (tháng đầu → thành thạo) | 420 → 234 | 330 → 187 | 330 → 187 |
| Video dài / ngày / người (thành thạo) | 1,6 | 2,0 | 2,0 |

**Đánh giá:** nhanh hơn ~20% nhưng đắt hơn 1,5–3 lần. Khi chạy cả 2 kênh, mỗi giờ tiết kiệm tốn 0,57–1,34 triệu ₫ — gấp 6–14 lần chi phí nhân sự/giờ (~97 nghìn ₫, giả định lương 15 triệu). **Nếu Kênh B không mở**, hạ được Flow Ultra → AI Pro và ElevenLabs Pro → Creator (−US$257/tháng) → chênh lệch ròng chỉ **−1,5 đến +5,8 triệu ₫/tháng** — khi đó đáng cân nhắc.

**Điểm yếu cần đo trong video thử:** B-roll lấy từ kho dễ rập khuôn (rủi ro "inauthentic content"); zoom/khoanh vùng màn hình trong trình dựng có thể kém CapCut; phụ thuộc 1 nhà cung cấp. **Không dùng cho Kênh B** (không người dẫn AI).

**Cách thử A/B (19–20/10):**
1. Ngày 16/10, nếu gói Creator không có Video Agent hoặc không đủ credit (1 video 18 phút cần 468–936 credit), nâng HeyGen lên **Pro 1.000 credit (US$49, thêm US$20 ngoài gói A)** cho tuần thử.
2. Video thử #1 (19/10): quy trình hiện tại. Video thử #2 (20/10): Video Agent + trình dựng, cùng dạng sản phẩm.
3. Ghi lại cho mỗi video: **phút thao tác bước 5–8**, **credit trước/sau** (trang Usage của HeyGen), số lỗi ở Cổng 2.
4. Ngày 21/10 sếp xem 2 video, chốt Q9. **Đổi sang HeyGen nếu:** đạt Cổng 2 ngang video #1 **và** chi phí tăng ròng ≤ giá trị giờ công tiết kiệm (~0,9 triệu ₫/tháng = 9,4 giờ × ~97 nghìn ₫). Nhập credit/phút thật vào ô ThongSo!B50–B51 để bảng tính tự tính lại.

