# THƯ VIỆN PROMPT

> Dùng trong Claude Project của kênh (đã có Bible trong Project knowledge). Phần trong `[ ]` là chỗ điền. Prompt cho Claude viết bằng tiếng Việt cũng được — Claude vẫn xuất nội dung tiếng Anh theo Bible.

## 1. Chọn chủ đề tuần
```text
Đề xuất 10 chủ đề video dài cho tuần [số tuần], theo Bible kênh, phân bổ đúng tần suất series.
Với mỗi chủ đề: tiêu đề tạm (≤ 60 ký tự), câu hỏi trung tâm, góc kể khác biệt so với 5 video top đầu trên YouTube,
điểm 1–5 cho: độ tò mò, mức cạnh tranh (5 = ít), số "khoảnh khắc ồ" để cắt short, độ chắc chắn của nguồn.
Loại bỏ chủ đề trùng với danh sách đã làm: [dán danh sách mã + tiêu đề đã đăng].
Xuất bảng, sắp xếp theo tổng điểm. Sau đó với chủ đề số 1, điền brief theo mẫu brief-video.md kèm 5 nguồn có link.
```

## 2. Viết kịch bản (gọi skill)
```text
Dùng skill kich-ban-video cho brief sau. Cấp chất lượng: [Tiêu chuẩn]. Độ dài mục tiêu: [10] phút.
[dán brief đã duyệt]
```
Sau đó:
```text
Dùng skill qc-video soát kịch bản và shot list vừa viết. Sửa luôn các lỗi mức "Phải sửa", liệt kê lỗi mức "Nên sửa" để tôi chọn.
```

## 3. Prompt ảnh — Nano Banana Pro
**Cấu trúc:** `[Chủ thể + hành động] , [bối cảnh + thời đại] , [góc máy] , [ánh sáng/không khí] , [chuỗi phong cách Bible]`

Ví dụ:
```text
A caravan of camels approaching a walled desert city at dusk, ancient Arabia around 300 A.D., wide establishing shot from a dune ridge, long shadows and drifting sand, cinematic historical reconstruction, painterly realism, warm golden-hour light, muted earth tones with teal shadows, 35mm film grain, volumetric haze, subject centered, centered composition, no text, no letters, no watermark, no logos, no modern objects
```
Giữ nhân vật nhất quán: tải 1–3 ảnh tham chiếu nhân vật trong `00_BIBLE/ref/` rồi thêm: `Use the attached reference image for the character's face, hair and clothing. Keep them identical.`

## 4. Prompt video — Veo 3.1 (Flow)
**Cấu trúc:** `[Chuyển động máy] + [chủ thể làm gì] + [môi trường chuyển động] + [âm thanh môi trường nếu cần] + [chuỗi phong cách]`

Từ vựng chuyển động máy hay dùng: `slow dolly-in`, `slow aerial flyover`, `slow pan left`, `static locked-off shot`, `gentle handheld drift`, `crane shot rising`, `orbit around the subject`.

Ví dụ (image-to-video từ keyframe ảnh mục 3):
```text
Slow aerial flyover toward the city gates as the caravan moves forward, sand blowing across the dunes, torches flickering on the walls, ambient wind sound only, no dialogue, no music. Cinematic historical reconstruction, painterly realism, warm golden-hour light, subject centered, no text.
```
Quy tắc:
- Luôn ghi `no dialogue, no music` (giọng và nhạc thêm ở bước dựng).
- Một clip = **một hành động đơn giản**. Hành động phức tạp → tách 2 clip.
- Short native cần dọc: chọn tỷ lệ **9:16** trong Flow (Ingredients to Video hỗ trợ dọc gốc).
- Model: Lite cho cảnh nền/phong cảnh; Fast cho cảnh có nhân vật; Quality chỉ cho cảnh hook (cấp Cao cấp).

## 5. Thumbnail
```text
Đề xuất 3 ý tưởng thumbnail cho video "[tiêu đề]". Mỗi ý tưởng: mô tả hình (1 chủ thể + 1 yếu tố bí ẩn), chữ trên thumbnail ≤ 4 từ,
bố cục (chủ thể bên nào, chữ bên nào), và prompt Nano Banana Pro tỷ lệ 16:9 theo chuỗi phong cách Bible (không có chữ trong ảnh — chữ thêm sau).
3 ý tưởng phải khác nhau rõ rệt để A/B test.
```

## 6. Phân tích số liệu hằng tuần
*Xuất từ YouTube Studio → Analytics → Advanced mode → Export (CSV), 28 ngày gần nhất, chia theo video.*
```text
Đây là số liệu YouTube Studio 28 ngày gần nhất [đính kèm CSV] và bảng KPI mục tiêu [dán dòng mục tiêu sheet KPI].
1) Viết báo cáo 5 dòng theo mẫu ở docs/10 mục 4.
2) So sánh 3 video tốt nhất với 3 video kém nhất: khác nhau ở chủ đề, tiêu đề, thumbnail, giữ chân 30 giây đầu, độ dài?
3) Đề xuất đúng 3 việc cần làm tuần tới, mỗi việc đo được bằng KPI nào.
4) Nếu thấy quy tắc nào trong Bible nên đổi, đề xuất câu chữ cụ thể để tôi cập nhật.
```

## 7. Sửa ảnh/clip bị lỗi
```text
Ảnh/clip cảnh [S0xx] bị lỗi: [mô tả: tay biến dạng / nhân vật khác mặt / có chữ lạ / chuyển động giật].
Prompt cũ: [dán]. Viết lại prompt để tránh lỗi này (đổi góc máy, bỏ chi tiết gây lỗi), giữ nguyên ý cảnh và chuỗi phong cách.
Nếu lỗi này có thể lặp lại ở video khác, đề xuất 1 quy tắc thêm vào Bible.
```

## 8. Short native
```text
Từ video "[tiêu đề]" (kịch bản đính kèm), viết 1 kịch bản short native 30–45 giây dạng "Did you know…":
câu đầu ≤ 10 từ gây tò mò, 3–4 câu nội dung, câu cuối là twist + gợi ý xem video đầy đủ.
Kèm shot list 4–6 cảnh dọc 9:16 có prompt ảnh và prompt Veo theo Bible.
```

## 9. Tên kênh & nhận diện (dùng 1 lần)
```text
Đề xuất 10 tên kênh YouTube tiếng Anh cho ngách History & Mysteries, khán giả toàn cầu.
Tiêu chí: 2–3 từ, dễ đọc, dễ nhớ, không trùng kênh lớn đã có, không chứa từ "AI", có thể đăng ký tên miền .com và handle @.
Với mỗi tên: ý nghĩa, rủi ro trùng lặp cần kiểm tra, ý tưởng logo (mô tả + prompt Nano Banana Pro).
```
