# BIBLE KÊNH — [Tên kênh]  ·  v1.0 (điền ngày)

> "Hiến pháp" của kênh. Mọi kịch bản, prompt, thumbnail phải theo tài liệu này. **Tải file này vào Project knowledge của Claude.** Khi phát hiện lỗi lặp lại → sửa ở đây trước, ghi vào mục 12 (Nhật ký thay đổi).
>
> Ví dụ dưới đây đã điền sẵn cho ngách đề xuất **Lịch sử & Bí ẩn** — chỉnh lại sau khi chốt ở buổi review.

## 1. Định vị kênh
| Mục | Nội dung |
|---|---|
| Tên kênh | [Tên kênh] |
| Ngách | History & Mysteries (series phụ: Myths & Legends) |
| Lời hứa với khán giả | *Cinematic stories of lost worlds and unsolved mysteries — told in about 10 minutes, backed by real sources.* |
| Khán giả | 25–54 tuổi, Mỹ/Anh/Canada/Úc/châu Âu; tò mò, thích phim tài liệu; xem video dài trên TV/máy tính, short trên điện thoại |
| Khác biệt | Tái hiện quá khứ bằng hình ảnh điện ảnh (điều quay thật không làm được) + kể chuyện chặt chẽ có nguồn |
| Không làm | Tin tức, chính trị hiện đại, tài chính/y tế/pháp lý, deepfake người thật, nội dung gây sốc/thao túng cảm xúc |

## 2. Giọng văn (tiếng Anh)
- Người kể chuyện điềm tĩnh, tò mò, thông minh — như người dẫn phim tài liệu, **không** như người bán hàng.
- Câu ngắn (trung bình 12–16 từ). Chi tiết cụ thể (con số, địa danh, vật thể) thay vì tính từ chung chung.
- Mỗi chương mở bằng **một câu hỏi hoặc một hình ảnh cụ thể**; kết bằng **một sự thật bất ngờ**.
- Thỉnh thoảng gọi trực tiếp người xem ("Imagine you're standing…") — tối đa 2 lần/video.
- Điều chưa chắc chắn: *"Historians believe…", "One theory suggests…", "We may never know…"*. Không khẳng định giả thuyết như sự thật.

### Từ & cụm từ cấm (văn phong "AI" sáo rỗng)
`delve`, `tapestry`, `testament to`, `in today's fast-paced world`, `buckle up`, `let's dive in`, `it's important to note`, `game-changer`, `ladies and gentlemen`, `unlock the secrets`, `shrouded in mystery` (tối đa 1 lần/kênh/tháng), `fascinating` (tối đa 1 lần/video), `journey` (nghĩa bóng).

### Không làm
- Không "clickbait nói dối": tiêu đề/thumbnail hứa điều gì, video phải trả lời điều đó.
- Không kêu gọi "like & subscribe" ở đầu video; chỉ 1 lời kêu gọi nhẹ ở cuối.

## 3. Cấu trúc kịch bản video dài (bắt buộc)
| Phần | Thời lượng | Quy tắc |
|---|---|---|
| Cold open (hook) | 0:00–0:30 | Bí ẩn/khoảnh khắc mạnh nhất; không giới thiệu kênh |
| Lời hứa | 0:30–0:50 | Người xem sẽ biết điều gì |
| Chương 1…6–8 | 60–90 giây/chương | Đứng độc lập; câu đầu không bắt đầu bằng "And", "So", "As we saw"; kết bằng twist |
| Cao trào / lời giải | 60–90 giây | Trả lời câu hỏi ở hook |
| Kết | 15–20 giây | Gợi ý 1 video liên quan của kênh |

Tổng 1.400–1.600 từ ≈ 10 phút (150 từ/phút).

## 4. Phong cách hình ảnh
**Chuỗi phong cách (dán vào cuối MỌI prompt ảnh/video):**
```
cinematic historical reconstruction, painterly realism, warm golden-hour light, muted earth tones with teal shadows, 35mm film grain, volumetric haze, subject centered, centered composition, no text, no letters, no watermark, no logos, no modern objects
```
| Quy tắc | Chi tiết |
|---|---|
| Bố cục | Chủ thể ở giữa khung (để cắt 9:16 được) |
| Góc máy ưu tiên | Toàn cảnh, trung cảnh, flycam chậm, dolly-in chậm |
| Tránh | Cận cảnh bàn tay, khuôn mặt đang nói, chữ viết, đám đông chen chúc |
| Ảnh tham chiếu | Thư mục `00_BIBLE/ref/` — 5 ảnh phong cách chuẩn; mỗi nhân vật lặp lại có 3 ảnh (chính diện, nghiêng, toàn thân) |
| Chuyển cảnh đặc trưng | Bản đồ cổ cuộn/la bàn (template CapCut) |

## 5. Giọng đọc
| Mục | Giá trị |
|---|---|
| Công cụ | ElevenLabs |
| Giọng | [Tên giọng] — Voice ID: `[điền]` |
| Model | Model đa ngôn ngữ chất lượng cao (không dùng model "Flash" cho video dài) |
| Thiết lập | Stability ~50%, Similarity ~75%, Style ~15%, tốc độ 1.0 (ghi lại thiết lập thực tế sau khi thử) |
| Nghỉ giữa chương | 0,5–0,8 giây |

### Quy tắc viết bản đọc (cho giọng AI)
- Viết số thành chữ: `1177 BC` → `eleven seventy-seven B.C.`; `3,000` → `three thousand`; `5th century` → `fifth century`.
- Viết đầy đủ chữ viết tắt: `approx.` → `approximately`; `km` → `kilometers`.
- Tên riêng khó: dùng cách viết phiên âm ở bảng 6 trong **bản đọc** (bản phụ đề vẫn giữ chính tả gốc).

## 6. Từ điển phát âm (bổ sung dần)
| Chính tả (phụ đề) | Viết cho giọng đọc |
|---|---|
| Göbekli Tepe | geh-BECK-lee TEH-peh |
| Ubar | oo-BAR |
| Herodotus | heh-ROD-uh-tus |
| Hatshepsut | hat-SHEP-soot |
| Ramesses | RAM-uh-seez |
| Teotihuacan | tay-oh-tee-wah-KAHN |
| Ragnarök | RAG-nuh-rok |
| Yggdrasil | IG-druh-sil |
| Xerxes | ZURK-seez |
| cuneiform | kyoo-NEE-uh-form |

## 7. Phụ đề & chữ trên hình
| | Video dài | Short |
|---|---|---|
| Hình thức | File SRT tải lên YouTube | Cháy vào hình |
| Font | [Font kênh, ví dụ Inter SemiBold] | [Ví dụ Montserrat ExtraBold] |
| Màu | Trắng, viền đen | Trắng viền đen; từ khoá vàng `#FFD400` |
| Giới hạn | ≤ 42 ký tự/dòng, ≤ 2 dòng | 1–4 từ/lần hiện, vị trí 1/3 dưới, chừa lề phải 15% |

## 8. Thumbnail & tiêu đề
- Thumbnail: **1 chủ thể + 1 yếu tố bí ẩn**, tối đa **4 từ**, tương phản cao, tông vàng–xanh ngọc của kênh, đọc được ở kích thước 160 px.
- Tiêu đề: **≤ 60 ký tự**, từ khoá chính trong 40 ký tự đầu; công thức: *Tò mò + Cụ thể* — "The City That Vanished Under the Sand", "What Really Happened to the Sea Peoples?".
- Luôn làm **3 phương án** thumbnail để dùng tính năng thử nghiệm A/B của YouTube.

## 9. Âm nhạc & âm thanh
- Nhạc chủ đề riêng: [tên bài Suno, tạo khi đang là thành viên Pro — lưu link]. Nhạc nền: YouTube Audio Library (thể loại Cinematic/Ambient).
- Nhạc nền thấp hơn giọng ~18–20 dB; xuất -14 LUFS.
- Tắt âm thanh gốc của clip Veo, trừ tiếng môi trường đã chọn.
- **Không dùng nhạc trong thư viện CapCut cho YouTube.**

## 10. Công khai nội dung AI
- Cảnh tái hiện **chân thực** → bật "Altered or synthetic content" khi đăng + dòng cuối mô tả: *"Visuals are AI-generated reconstructions for illustration."*
- Phong cách kỳ ảo/thần thoại rõ ràng → không bắt buộc bật nhãn, vẫn giữ dòng mô tả.

## 11. Danh mục series
| Series | Mô tả | Tần suất |
|---|---|---|
| Lost Worlds | Nền văn minh/thành phố biến mất | 2/tuần |
| Unsolved | Bí ẩn chưa có lời giải | 1/tuần |
| Daily Life In… | Cuộc sống thường ngày thời cổ đại | 1/tuần |
| Myths Retold | Thần thoại kể như phim (phong cách kỳ ảo) | 1/tuần |

## 12. Nhật ký thay đổi Bible
| Ngày | Thay đổi | Lý do (mã lỗi / số liệu) |
|---|---|---|
| | v1.0 tạo mới | — |
