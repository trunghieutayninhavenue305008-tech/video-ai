# 04 — Quy trình sản xuất (Claude là "bộ não")

## 1. Sơ đồ tổng thể

```
[1] Chọn sản phẩm ──► [2] Dùng thử + quay màn hình ──► [3] Kịch bản + shot list ──► (CỔNG 1: nội dung + tuân thủ)
  Claude + skill           Người/Claude in Chrome          Claude (skill)              Người + Claude qc-video
  affiliate research                                                                        │
                                                                                            ▼
[9] SEO + link + disclosure ◄── [8] Dựng ◄── [7] B-roll người AI ◄── [6] Người dẫn AI ◄── [5] Giọng đọc
  Claude seo-xuat-ban            CapCut       Veo 3.1 / Nano Banana    HeyGen (chỉ Kênh A)   ElevenLabs
        │
        ▼
 (CỔNG 2: QC video + tuân thủ) ──► Hẹn giờ đăng ──► Cắt 5 short (tool Claude) ──► Hẹn giờ short
 Thứ Hai: Claude phân tích YouTube Studio + dashboard affiliate → chọn sản phẩm tuần sau, cập nhật Bible
```

**Nguyên tắc:** AI tạo toàn bộ hình, giọng, dựng; **dữ liệu sản phẩm là thật**; con người **chọn – test – duyệt**.

## 2. Chi tiết 10 bước

Thời gian = phút thao tác của 1 người cho 1 video ~18 phút, cấp Tiêu chuẩn (tháng đầu → thành thạo). Tổng **420 → 234 phút**.

### Bước 1 — Chọn sản phẩm & nghiên cứu (45 → 25 phút)
- **Claude** + skill có sẵn **`saas-affiliate-research`** (SaaS/AI có affiliate), **`broker-affiliate-research`** / **`forex-broker`** (sàn/broker, giấy phép, chương trình đối tác).
- Tiêu chí chọn: có chương trình affiliate (đã được duyệt hoặc đang xin), có nhu cầu tìm kiếm, có bản dùng thử/gói rẻ để test, **Kênh B: giấy phép cấp 1** (FCA, ASIC, CySEC…) và không nằm trong danh sách cảnh báo.
- Đầu ra: `brief.md` theo [mẫu](../templates/brief-video.md) — tính năng, bảng giá (ghi ngày), 3 đối thủ, điểm khen/chê phổ biến của người dùng (có link nguồn), danh sách cảnh cần quay.

### Bước 2 — Dùng thử & quay màn hình (60 → 40 phút) — *dữ liệu thật*
- Tạo tài khoản dùng thử/gói rẻ; thao tác theo **danh sách cảnh cần quay** trong brief; quay bằng **OBS** (miễn phí) hoặc trình ghi của CapCut, 1080p 30fps.
- Tuỳ chọn: **Claude in Chrome** thao tác trên web app theo kịch bản trong khi OBS ghi hình.
- Ghi lại **kết quả test có số liệu** (thời gian xử lý, chất lượng đầu ra, lỗi gặp phải) — kịch bản chỉ được khẳng định những gì có trong ghi chú này.
- Kênh B: tài khoản thật, nạp số tiền nhỏ, chụp phí/spread thật, thử rút tiền, lưu bằng chứng.

### Bước 3 — Kịch bản module + shot list (45 → 25 phút)
- **Skill `kich-ban-video`**: lời thoại tiếng Anh 2.250–3.000 từ, chia vai **HOST** (người dẫn AI) / **VO** (lời kể trên hình), shot list với loại cảnh `host | screen | broll | graphic | product`, prompt Veo/Nano Banana, câu công khai & cảnh báo đặt sẵn đúng chỗ, 5 phần đề xuất làm short.

### CỔNG 1 — Duyệt kịch bản & tuân thủ (20 → 10 phút)
- **Skill `qc-video`** chạy trước → người duyệt theo [checklist](../templates/checklist-qc.md#cổng-1--kịch-bản--tuân-thủ).
- Trọng tâm: mọi khẳng định có trong ghi chú test hoặc nguồn; **không câu nào tự nhận trải nghiệm không có thật**; disclosure; Kênh B: cảnh báo rủi ro, không lời khuyên đầu tư, không hứa lợi nhuận.

### Bước 4 — Giọng đọc (25 → 12 phút)
- **ElevenLabs**, 1 giọng cố định của kênh. Xuất **2 nhóm file**: `host_*.mp3` (lời người dẫn) và `vo_*.mp3` (lời kể trên hình). Từ điển phát âm tên sản phẩm trong Bible.

### Bước 5 — Người dẫn AI (30 → 15 phút) — *chỉ Kênh A*
- **HeyGen Avatar IV**: tải file `host_*.mp3` → avatar cố định của kênh tự khớp khẩu hình. Xuất 16:9 cho video dài, 9:16 cho short native.
- Avatar được tạo **1 lần** từ ảnh nhân vật hư cấu (Nano Banana Pro), lưu trong Bible.

### Bước 6 — Cảnh người thật AI + ảnh (45 → 25 phút)
- **Nano Banana Pro** tạo keyframe → **Veo 3.1** (Flow) tạo clip 8 giây: người dùng sản phẩm, làm việc, phản ứng. Prompt theo chuỗi phong cách "photorealistic" của Bible; tránh cận tay, tránh người đang nói.
- SPVL: dùng ảnh sản phẩm thật làm ảnh tham chiếu.

### Bước 7 — Dựng (100 → 55 phút)
- **CapCut Pro** với template kênh: ráp theo file giọng; đoạn màn hình có **zoom vào chỗ thao tác**, con trỏ nổi bật; bảng giá/so sánh từ template; lớp người dẫn; phụ đề **lấy từ kịch bản**; nhạc nền hạ âm; dòng công khai ở 30 giây đầu.

### Bước 8 — Thumbnail, SEO, link affiliate (30 → 15 phút)
- **Skill `seo-xuat-ban`**: 3 tiêu đề, mô tả mở đầu bằng **công khai affiliate**, link (qua trang trung gian/link rút gọn có lọc quốc gia cho Kênh B), chapter, cảnh báo rủi ro (Kênh B), 3 thumbnail (Kênh A: mặt người dẫn + logo/giao diện sản phẩm).

### CỔNG 2 — QC, xuất, hẹn giờ (20 → 12 phút)
- [Checklist cổng 2](../templates/checklist-qc.md#cổng-2--video-hoàn-chỉnh--xuất-bản): hình/âm/phụ đề, **bật nhãn "Altered or synthetic content"** (bắt buộc với người dẫn AI trông như thật), tick "Paid promotion" nếu nhận tiền/sản phẩm từ hãng, link đúng, hẹn giờ.

### Sau đăng — Cắt 5 short (40 → 25 phút)
- `tools/cat_short.py` (đoạn màn hình dùng `--mode blur`; Kênh B thêm `--note "Not financial advice · Capital at risk"`) hoặc OpusClip → duyệt nhanh → hẹn giờ.

### Thứ Hai — Phân tích (30 phút)
- Claude đọc CSV YouTube Studio + báo cáo click/chuyển đổi affiliate → 5 dòng báo cáo + 3 việc tuần tới + sản phẩm nên review tiếp (dựa trên chuyển đổi thật).

## 3. Cấu trúc thư mục & đặt tên

```
KENH-A/  KENH-B/
├── 00_BIBLE/            Bible, avatar người dẫn (ảnh gốc + ID HeyGen), giọng (Voice ID), template CapCut
├── 01_SAN-PHAM/         danh sách sản phẩm & trạng thái chương trình affiliate
└── VIDEO/V001_notion-ai-review/
    ├── 1_brief/          brief.md, ghi-chu-test.md (số liệu test thật + ảnh chụp bằng chứng)
    ├── 2_screen/         SCR01.mp4 … (quay màn hình thật)
    ├── 3_script/         script.md, shotlist.csv
    ├── 4_voice/          host_01.mp3 … vo_01.mp3 …
    ├── 5_host/           host_01.mp4 … (HeyGen)
    ├── 6_broll/          S012_v1.mp4 … (Veo)
    ├── 7_edit/           project CapCut
    ├── 8_export/         final_16x9.mp4, subtitles.srt, thumb_A/B/C.png, seo.md
    └── 9_shorts/         short_01.mp4 … shorts.csv
```

## 4. Vì sao quy trình này giữ được kiếm tiền & an toàn pháp lý

| Yêu cầu | Quy trình đáp ứng |
|---|---|
| YouTube: không rập khuôn hàng loạt | Mỗi video 1 sản phẩm, dữ liệu test riêng, demo riêng |
| YouTube: không AI persona tư vấn tài chính | Kênh B không có người dẫn AI; nội dung dữ kiện, không lời khuyên |
| YouTube: công khai nội dung tổng hợp trông như thật | Bật nhãn ở mọi video có người dẫn AI/cảnh người AI |
| FTC: không review giả, công khai quan hệ tài chính | Chỉ khẳng định điều đã test; công khai bằng lời + chữ + mô tả |
| Pháp luật tài chính (VN, UK, EU, US) | Kênh B chờ ý kiến luật sư; lọc quốc gia; chỉ sàn giấy phép cấp 1; cảnh báo rủi ro |
