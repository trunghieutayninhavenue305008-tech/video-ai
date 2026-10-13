# THƯ VIỆN PROMPT (kênh review)

> Dùng trong Claude Project của từng kênh (Bible đã có trong Project knowledge). Phần `[ ]` là chỗ điền. Viết yêu cầu bằng tiếng Việt cũng được — Claude xuất nội dung tiếng Anh theo Bible.

## 1. Chọn sản phẩm tuần
```text
Dùng skill saas-affiliate-research (Kênh A) / broker-affiliate-research và forex-broker (Kênh B).
Đề xuất 10 sản phẩm để review tuần [số tuần] cho kênh [A/B], theo Bible và tần suất series.
Mỗi sản phẩm: tên, website, chương trình affiliate (hoa hồng, cookie, điều kiện), có bản dùng thử/gói rẻ để test không,
nhu cầu tìm kiếm ước tính, 3 đối thủ, dạng video đề xuất (review đơn / head-to-head / best-of).
Kênh B thêm: cơ quan cấp phép + số giấy phép + link tra cứu; có trong danh sách cảnh báo FCA/AMF không; quốc gia không phục vụ.
Loại bỏ sản phẩm đã làm: [dán danh sách]. Xuất bảng xếp hạng, rồi điền brief-video.md cho sản phẩm số 1 (để trống phần GHI CHÚ TEST).
```

## 2. Danh sách cảnh cần quay (trước Bước 2)
```text
Từ brief V[___], lập danh sách 15–25 cảnh quay màn hình cần có để chứng minh từng khẳng định trong video:
mỗi cảnh ghi: mã SCRxx, màn hình/thao tác, dữ liệu cần thấy rõ, thời lượng gợi ý, phần kịch bản dùng đến.
Thêm 5 phép test có số liệu (ví dụ: thời gian tạo 1 video, độ chính xác, giới hạn gói Free).
```

## 3. Tạo người dẫn AI (1 lần)
**Nano Banana Pro — ảnh gốc người dẫn (Kênh A):**
```text
Photorealistic studio portrait of a fictional tech reviewer in their early 30s, friendly and confident expression, smart-casual neutral-colored shirt, modern home studio background with soft warm lighting, blurred monitor and plant behind, chest-up framing, looking at camera, natural skin texture, 50mm lens, subject centered, no text, no logos
```
Sau đó tạo thêm 3 góc (nghiêng trái/phải, trung cảnh) bằng ảnh gốc làm tham chiếu: `Use the attached image as the same person. Keep face, hair and outfit identical.` → kiểm tra không giống người thật (Google Lens) → tạo Avatar trên HeyGen → lưu Avatar ID vào Bible.

## 4. Viết kịch bản (gọi skill)
```text
Dùng skill kich-ban-video. Kênh: [A/B]. Cấp: [Tiêu chuẩn]. Độ dài mục tiêu: [18] phút. Dạng: [review đơn / head-to-head / best-of].
Brief: [dán brief]
Ghi chú test: [dán ghi-chu-test.md]
```
Sau đó:
```text
Dùng skill qc-video soát kịch bản và shot list vừa viết, đối chiếu ghi chú test. Sửa luôn lỗi "Phải sửa", liệt kê lỗi "Nên sửa".
```

## 5. Cảnh người thật AI — Veo 3.1 (Flow)
**Cấu trúc:** `[chuyển động máy] + [người làm 1 hành động đơn giản] + [bối cảnh] + no dialogue, no music + [chuỗi phong cách Bible]`

Ví dụ Kênh A:
```text
Slow dolly-in on a young marketer working on a laptop at a sunny co-working desk, she leans back and smiles at the screen, coffee cup beside her, no dialogue, no music. Photorealistic, natural skin texture, candid documentary style, soft daylight, shallow depth of field, subject centered, no text, no logos
```
Ví dụ Kênh B (minh hoạ, không nhìn ống kính, không nói):
```text
Static side-angle shot of a person reviewing price charts on two monitors in a dim home office at night, screen glow on their face, they take notes in a notebook, no dialogue, no music. Photorealistic, candid, shallow depth of field, subject centered, no readable text on screens, no logos
```
Quy tắc: 1 clip = 1 hành động; tránh cận tay; không chữ đọc được trên màn hình giả (màn hình thật dùng bản quay OBS).

**SPVL — người dùng sản phẩm từ ảnh thật (Nano Banana Pro → Veo):**
```text
Use the attached official product photo. Show a creator in a home studio speaking into this exact microphone on a desk boom arm; keep the product's shape, color and logo placement exactly as in the reference. Photorealistic, soft daylight, subject centered, no added text.
```
→ chèn chữ `Illustration` góc dưới khi dựng.

## 6. Thumbnail
```text
Đề xuất 3 thumbnail khác biệt rõ cho video "[tiêu đề]" (kênh [A/B]).
Mỗi phương án: chữ ≤ 4 từ, bố cục, biểu cảm người dẫn (Kênh A) hoặc yếu tố dữ kiện (Kênh B: con số phí, huy hiệu giấy phép),
và prompt Nano Banana Pro 16:9 (không có chữ/logo trong ảnh — chữ và logo thật thêm sau ở CapCut).
Kênh B: không dùng mặt người kiểu "chuyên gia tư vấn".
```

## 7. Phân tích số liệu hằng tuần
*YouTube Studio → Analytics → Advanced → Export CSV (28 ngày, theo video) + báo cáo click/chuyển đổi từ các chương trình affiliate.*
```text
Đây là số liệu YouTube Studio 28 ngày [đính kèm], báo cáo affiliate [đính kèm] và dòng mục tiêu sheet KPI [dán].
1) Báo cáo 5 dòng theo mẫu docs/10 mục 4.
2) Xếp hạng video theo doanh thu affiliate / 1.000 lượt xem và theo giờ xem — điểm chung của 3 video tốt nhất?
3) Đề xuất 3 việc tuần tới (đo được bằng KPI nào) và 5 sản phẩm nên review tiếp dựa trên chuyển đổi thật.
4) Video cũ nào cần cập nhật giá/link/bình luận ghim?
5) Quy tắc Bible nào nên đổi — đề xuất câu chữ cụ thể.
```

## 8. Sửa ảnh/clip lỗi
```text
Cảnh [S0xx] lỗi: [tay biến dạng / người đổi mặt / chữ lạ / sản phẩm sai hình dạng].
Prompt cũ: [dán]. Viết lại prompt tránh lỗi (đổi góc máy, bỏ chi tiết gây lỗi), giữ ý cảnh và chuỗi phong cách.
Nếu lỗi có thể lặp lại, đề xuất 1 quy tắc thêm vào Bible.
```

## 9. Short native
```text
Từ video "[tiêu đề]" (kịch bản đính kèm), viết 1 short native 30–45 giây dạng "[3 things… / X vs Y in 40 seconds / The real price of…]":
câu đầu ≤ 10 từ, 3–4 câu nội dung chỉ dùng dữ liệu đã test, câu cuối là cú chốt + gợi ý xem bản đầy đủ.
Kênh A: lời người dẫn (HeyGen 9:16) + 2–3 cảnh màn hình. Kênh B: lời kể + màn hình + dòng "Not financial advice · Capital at risk".
```

## 10. Cập nhật video cũ khi giá/ưu đãi đổi
```text
[Sản phẩm] đổi giá: [cũ] → [mới] từ [ngày]. Soạn bình luận ghim cập nhật (≤ 2 câu, tiếng Anh) và dòng sửa trong mô tả cho các video: [danh sách mã].
```

## 11. Tên kênh & nhận diện (dùng 1 lần)
```text
Đề xuất 10 tên kênh YouTube tiếng Anh cho [Kênh A: review SaaS & AI tool | Kênh B: review sàn crypto & broker forex].
Tiêu chí: 2–3 từ, dễ nhớ, gợi "trung thực/test thật", không chứa từ "AI" (Kênh B không chứa "profit/rich/signal"), kiểm tra được tên miền .com và handle @.
Mỗi tên: ý nghĩa, rủi ro trùng lặp cần kiểm tra, ý tưởng logo + prompt Nano Banana Pro.
```
