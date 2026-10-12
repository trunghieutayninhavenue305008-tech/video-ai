# 04 — Quy trình sản xuất 100% AI (Claude là "bộ não")

## 1. Sơ đồ tổng thể

```
 [1] Chủ đề ──► [2] Kịch bản + shot list ──► (CỔNG 1) ──► [3] Giọng đọc ─┐
   Claude         Claude (skill)              Người+Claude   ElevenLabs   │
                                                                          ▼
 [9] Đăng & hẹn giờ ◄── (CỔNG 2) ◄── [7] Thumbnail+SEO ◄── [6] Dựng ◄── [4] Ảnh ──► [5] Clip video
  YouTube/Meta/TikTok   Người+checklist  Claude+Nano Banana   CapCut     Nano Banana   Veo 3.1 / Kling
        │
        └──► [8] Cắt 5 short (tool Claude cat_short.py / OpusClip) ──► (Cổng 2 rút gọn) ──► đăng
 [10] Thứ Hai hằng tuần: Claude phân tích số liệu YouTube Studio → cập nhật Bible & danh sách chủ đề
```

**Nguyên tắc:** AI làm 100% phần tạo nội dung; con người **chọn – bấm – duyệt**. Mọi đầu ra của bước trước là **đầu vào chuẩn hoá** của bước sau (không ai phải "dịch" lại) → giảm lỗi lặt vặt.

## 2. Chi tiết từng bước

Thời gian = phút thao tác của 1 người cho 1 video dài 10 phút, cấp Tiêu chuẩn (tháng đầu → khi thành thạo). Tổng: **350 → 190 phút**.

### Bước 1 — Chọn chủ đề & nghiên cứu (30 → 15 phút)
- **Công cụ:** Claude (bật web search) trong Project của kênh; vidIQ bản miễn phí để xem lượng tìm kiếm.
- **Làm gì:** Claude đề xuất 10 chủ đề/tuần theo Bible kênh, chấm điểm (độ tò mò, độ cạnh tranh, khả năng cắt short), kèm **5–8 nguồn tham khảo có link** cho chủ đề được chọn.
- **Đầu ra:** `brief.md` theo mẫu [templates/brief-video.md](../templates/brief-video.md).
- **Xong khi:** brief có tiêu đề tạm, góc kể, 6–8 chương, nguồn kiểm chứng.

### Bước 2 — Kịch bản module + shot list + prompt (45 → 20 phút)
- **Công cụ:** Claude + **skill `kich-ban-video`** ([.claude/skills/kich-ban-video](../.claude/skills/kich-ban-video/SKILL.md)).
- **Làm gì:** 1 lần gọi ra trọn bộ: lời thoại tiếng Anh theo khung module (xem [03](03-dinh-dang-do-dai.md)), bảng shot list (mỗi cảnh: thời lượng, lời thoại, prompt ảnh, prompt video, loại model Lite/Fast/Quality), từ điển phát âm tên riêng, gợi ý 5 chương làm short.
- **Đầu ra:** `script.md` + `shotlist.csv`.
- **Xong khi:** đủ 1.400–1.600 từ (≈10 phút), mỗi chương đứng độc lập, mọi con số/tên riêng có nguồn.

### CỔNG 1 — Duyệt kịch bản (15 → 10 phút)
- **Công cụ:** Claude **skill `qc-video`** chạy trước, người duyệt sau theo [checklist](../templates/checklist-qc.md#cổng-1--kịch-bản).
- **Vì sao đặt cổng ở đây:** sửa 1 câu trong kịch bản mất 10 giây; sửa sau khi đã tạo giọng + hình + dựng mất 30 phút. **80% lỗi lặt vặt bị chặn ở cổng này.**

### Bước 3 — Giọng đọc (20 → 10 phút)
- **Công cụ:** ElevenLabs — 1 giọng cố định của kênh (Voice ID lưu trong Bible), model đa ngôn ngữ chất lượng cao.
- **Làm gì:** dán kịch bản đã duyệt (đã viết số thành chữ, đã chèn từ điển phát âm), tạo theo từng chương → nghe nhanh → tạo lại câu lỗi.
- **Đầu ra:** `voice_ch01.mp3 … voice_chNN.mp3` + bản ghép `voice_full.mp3`.

### Bước 4 — Ảnh nhân vật & keyframe (45 → 25 phút)
- **Công cụ:** Nano Banana Pro (Gemini 3 Pro Image) trong Gemini/Flow.
- **Làm gì:** dùng **ảnh tham chiếu cố định** (nhân vật, phong cách) đã lưu trong Bible; chạy prompt từ shot list. Ảnh tĩnh dùng trực tiếp (40%) hoặc làm khung đầu cho clip video (60%).
- **Quy tắc:** **không để AI vẽ chữ trong ảnh** (chữ AI hay sai chính tả) — chữ thêm ở bước dựng.

### Bước 5 — Tạo clip video (90 → 50 phút, phần lớn là chờ)
- **Công cụ:** **Veo 3.1 trong Flow** (chính) — Lite cho cảnh nền đơn giản, Fast cho cảnh chính, Quality chỉ cho cảnh "đinh" (cấp Cao cấp). **Kling** dự phòng cho cảnh cần chuyển động dài/điều khiển camera.
- **Làm gì:** "Frames/Ingredients to Video" từ keyframe bước 4 → giữ nhân vật nhất quán. Xếp hàng nhiều lệnh song song, trong lúc chờ làm bước 7.
- **Quy tắc:** **tắt/bỏ âm thanh gốc của Veo** cho cảnh nền (chỉ giữ tiếng động môi trường nếu tốt); tránh cận cảnh tay và mặt nói chuyện (AI hay lỗi ngón tay, khẩu hình).

### Bước 6 — Dựng (60 → 35 phút)
- **Công cụ:** CapCut Pro bản desktop với **template của kênh** (intro 3 giây, kiểu phụ đề, chuyển cảnh, preset xuất).
- **Làm gì:** kéo giọng đọc làm "xương sống" → đặt clip/ảnh theo shot list → phụ đề tự động **khớp từ kịch bản** (không dùng nhận dạng giọng nói để tránh sai chính tả) → nhạc nền (YouTube Audio Library/Suno) tự hạ âm khi có giọng → xuất 1080p.
- **Đầu ra:** `final_16x9.mp4` + `subtitles.srt`.

### Bước 7 — Thumbnail, tiêu đề, mô tả, chapter (25 → 15 phút)
- **Công cụ:** Claude **skill `seo-xuat-ban`** + Nano Banana Pro + CapCut/Canva để thêm chữ.
- **Đầu ra:** 3 phương án tiêu đề, 3 thumbnail (dùng tính năng thử nghiệm A/B thumbnail của YouTube), mô tả + chapter + hashtag, bình luận ghim, caption riêng cho từng nền tảng short.

### CỔNG 2 — QC video, xuất, lên lịch (20 → 10 phút)
- Xem tua nhanh toàn bộ theo [checklist cổng 2](../templates/checklist-qc.md#cổng-2--video-hoàn-chỉnh): hình lỗi, khoảng đen, âm lượng, phụ đề, thumbnail, **nhãn nội dung AI**.
- Hẹn giờ đăng (xem [07](07-nang-suat-lich-dang.md)).

### Bước 8 — Cắt 5 short (40 → 25 phút)
- **Công cụ:** **tool `tools/cat_short.py`** (Claude đọc phụ đề, chọn 5 đoạn hay nhất, ffmpeg tự cắt 9:16 + cháy phụ đề + viết tiêu đề/hashtag) hoặc **OpusClip** (bản thương mại, có điểm "viral" và tự hẹn giờ).
- **Đầu ra:** 5 file `short_01.mp4 …` + `shorts.csv` (tiêu đề, mô tả, hashtag từng nền tảng).
- Duyệt nhanh 5 short (xem hết mỗi short 1 lần) → hẹn giờ đăng.

### Bước 9 — Short native (45 → 30 phút/short)
- Claude viết kịch bản 30–45 giây dạng "Did you know…" từ chủ đề video dài → Veo 3.1 tạo **dọc 9:16 gốc** → CapCut template short.

### Bước 10 — Phân tích hằng tuần (thứ Hai, 30 phút)
- Xuất số liệu YouTube Studio (CSV) → Claude phân tích theo [prompt mẫu](../templates/thu-vien-prompt.md#6-phân-tích-số-liệu-hằng-tuần) → 3 việc cần làm tuần này + cập nhật Bible (lỗi nào lặp lại thì sửa ở gốc).

## 3. Cấu trúc thư mục & đặt tên (Google Drive)

```
KENH-1/
├── 00_BIBLE/                 Bible kênh, ảnh tham chiếu nhân vật, logo, font, template CapCut
├── 01_CHU-DE/                danh sách chủ đề tuần (Claude xuất)
└── VIDEO/
    └── V001_lost-city-of-ubar/
        ├── 1_brief/          brief.md
        ├── 2_script/         script.md, shotlist.csv
        ├── 3_voice/          voice_ch01.mp3 … voice_full.mp3
        ├── 4_images/         S001.png … (S = số cảnh trong shot list)
        ├── 5_clips/          S001_v1.mp4, S001_v2.mp4 …
        ├── 6_edit/           project CapCut
        ├── 7_export/         final_16x9.mp4, subtitles.srt, thumb_A/B/C.png, seo.md
        └── 8_shorts/         short_01.mp4 … shorts.csv
```

- Mã video `V001`, `V002`… trùng với cột "Mã video" trong sheet **TheoDoi** của bảng tính.
- Tên cảnh `S001`… trùng với số dòng trong `shotlist.csv` → tìm file không cần hỏi.

## 4. Vì sao quy trình này giữ được kiếm tiền trên YouTube

| Yêu cầu của YouTube | Quy trình đáp ứng thế nào |
|---|---|
| Không rập khuôn, mỗi video có câu chuyện riêng | Mỗi video 1 chủ đề nghiên cứu riêng, kịch bản riêng, cấu trúc chương khác nhau |
| Có giá trị giáo dục/kể chuyện, không phải "slideshow chữ chạy" | Kịch bản kể chuyện có nguồn kiểm chứng; 60% là cảnh chuyển động |
| Không sản xuất hàng loạt | Trần 1 video dài/ngày/kênh; con người chọn chủ đề và duyệt 2 cổng |
| Công khai nội dung AI trông như thật | Cổng 2 bắt buộc kiểm tra ô "Altered or synthetic content" |
