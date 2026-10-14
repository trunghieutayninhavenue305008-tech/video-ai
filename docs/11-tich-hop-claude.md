# 11 — Tích hợp Claude: "bộ não" của xưởng video review

> Claude là **trưởng nhóm nội dung + nhà nghiên cứu sản phẩm + biên tập viên tiếng Anh + kiểm soát tuân thủ + kỹ sư tự động hoá**. Con người chọn, test, duyệt.

## 1. Claude làm gì ở từng bước

| Bước | Claude làm | Hình thức |
|---|---|---|
| 1. Chọn sản phẩm | Tìm SaaS/AI tool có affiliate, đánh giá nhu cầu, đối thủ; Kênh B: tra giấy phép, chương trình đối tác | **Skill có sẵn của công ty:** `saas-affiliate-research`, `broker-affiliate-research`, `forex-broker` + web search |
| 2. Test sản phẩm | Lập danh sách cảnh cần quay; (tuỳ chọn) thao tác web app theo kịch bản | Claude Project; **Claude in Chrome** |
| 3. Kịch bản | Kịch bản module 15–20 phút, vai HOST/VO, shot list, câu công khai, cảnh báo | **Skill `kich-ban-video`** |
| Cổng 1 | Soát sự thật theo ghi chú test, câu bịa trải nghiệm, disclosure, cảnh báo, ngữ pháp | **Skill `qc-video`** |
| 6–7. Hình | Prompt người dẫn, cảnh người thật AI, thumbnail theo Bible | Claude Project + [thư viện prompt](../templates/thu-vien-prompt.md) |
| 9. SEO | Tiêu đề, mô tả (công khai ở dòng đầu), chapter, caption short 4 nền tảng | **Skill `seo-xuat-ban`** |
| Cắt short | Chọn 5 đoạn hay từ phụ đề, viết caption; ffmpeg cắt tự động | **Claude API** qua `tools/cat_short.py` |
| Phân tích | YouTube Studio + dashboard affiliate → báo cáo, chọn sản phẩm tuần sau theo chuyển đổi | Claude Project |
| Bảo trì | Sửa Bible/skill/template khi lỗi lặp lại; cập nhật giá/link video cũ | **Claude Code** trên repo |

## 2. Gói Claude

| Gói | Giá | Dùng khi |
|---|---|---|
| Pro | US$20/tháng | Tuần chuẩn bị (gói A) |
| **Max 5x** | **US$100/tháng** | **Gói B** — nghiên cứu sản phẩm, viết 5 kịch bản/tuần, QC, Claude Code |
| Max 20x | US$200/tháng | Gói C — 2 người |
| Claude API | Theo token | Tool cắt short — dưới US$0,10/video (Opus 5.5: US$4 / US$20 mỗi 1 triệu token vào/ra) |

## 3. Thiết lập 2 Claude Project (làm 1 lần, 20 phút mỗi kênh)

1. claude.ai → **Projects** → tạo `Kênh A — [Tên]` và `Kênh B — [Tên]`.
2. **Project knowledge**: `templates/kenh-bible.md` (bản đã điền cho kênh), `templates/thu-vien-prompt.md`, `templates/checklist-qc.md`, `docs/09-chinh-sach-phap-ly-rui-ro.md`, 2–3 kịch bản tốt nhất (bổ sung dần).
3. **Project instructions** — dán (sửa phần trong ngoặc):

```text
Bạn là trưởng nhóm nội dung của kênh YouTube tiếng Anh "[Tên kênh]" — review [SaaS, AI tool, sản phẩm công nghệ | sàn crypto và broker forex], khán giả toàn cầu.
- Tuân thủ Bible kênh trong Project knowledge: giọng văn, người dẫn, phong cách hình, câu công khai, từ cấm, phát âm.
- Nội dung xuất bản viết tiếng Anh Mỹ; giải thích và ghi chú cho đội ngũ viết tiếng Việt.
- Chỉ khẳng định những gì có trong ghi chú test của đội hoặc nguồn chính thức (kèm link, ngày). Không bao giờ bịa trải nghiệm, lời chứng thực hay số liệu.
- Luôn có công khai affiliate ở 30 giây đầu và dòng đầu mô tả.
- [Chỉ Kênh B] Không có người dẫn AI; không đưa lời khuyên đầu tư; không hứa lợi nhuận; luôn có cảnh báo rủi ro; chỉ sàn/broker có giấy phép cấp 1.
- Dùng skill kich-ban-video để viết kịch bản, qc-video để soát, seo-xuat-ban cho tiêu đề/mô tả.
- Nếu yêu cầu mơ hồ, chọn phương án hợp lý theo Bible và ghi giả định thay vì hỏi lại.
```

## 4. Cài skill

| Skill | Nguồn | Đầu ra |
|---|---|---|
| `kich-ban-video` | Repo — [.claude/skills/kich-ban-video](../.claude/skills/kich-ban-video/SKILL.md) | Kịch bản review module, bản đọc HOST/VO, shot list CSV, prompt, công khai, nguồn |
| `qc-video` | Repo — [.claude/skills/qc-video](../.claude/skills/qc-video/SKILL.md) | Bảng lỗi theo mã (gồm mã tuân thủ C1–C8), Đạt/Không đạt, đề xuất sửa gốc |
| `seo-xuat-ban` | Repo — [.claude/skills/seo-xuat-ban](../.claude/skills/seo-xuat-ban/SKILL.md) | Tiêu đề, mô tả có công khai, chapter, thumbnail, caption short |
| `saas-affiliate-research` | **Đã có** trong tài khoản Claude của công ty | Danh sách SaaS/AI tool có affiliate + phân tích |
| `broker-affiliate-research`, `forex-broker` | **Đã có** trong tài khoản Claude của công ty | Sàn/broker có affiliate, giấy phép, so sánh |

**Cài 3 skill của repo lên claude.ai:** nén từng thư mục (ví dụ `kich-ban-video/` chứa `SKILL.md`) thành `.zip` → **Settings → Capabilities → Skills → Upload skill**. **Với Claude Code:** chạy `claude` trong thư mục repo — skill trong `.claude/skills/` tự được nạp.

## 5. Claude Code & Claude in Chrome — tự động hoá không cần biết lập trình

Ví dụ câu lệnh tiếng Việt:
- *"Chạy tools/cat_short.py cho video V012, chế độ blur, thêm dòng 'Not financial advice · Capital at risk', rồi mở shorts.csv."*
- *"Đọc file analytics và báo cáo affiliate tuần này trong thư mục bao-cao/, viết báo cáo 5 dòng theo docs/10."*
- *"Giá gói Pro của [sản phẩm] vừa đổi — tìm các video có nhắc giá cũ trong thư mục VIDEO và soạn bình luận ghim cập nhật."*
- (Claude in Chrome) *"Mở [web app], làm theo danh sách cảnh trong brief V015, dừng 3 giây ở mỗi màn hình"* — trong khi OBS ghi hình.

## 6. Tool `cat_short.py`

Đầu vào: video dài + SRT. Claude chọn 5 đoạn 20–90 giây đứng độc lập; ffmpeg cắt 9:16 (`crop` cho đoạn người dẫn, `blur` cho đoạn màn hình), cháy phụ đề, `--note` thêm dòng cảnh báo cố định (Kênh B), xuất `shorts.csv` caption từng nền tảng. Chi tiết: [tools/README.md](../tools/README.md).

## 7. Nguyên tắc dùng Claude để ít phải sửa

1. Đưa đủ ngữ cảnh 1 lần: Bible + brief + **ghi chú test**.
2. Yêu cầu đầu ra có cấu trúc (skill đã làm sẵn).
3. Cho Claude tự soát (`qc-video`) trước khi người duyệt.
4. Lỗi lặp lại → sửa skill/Bible, không sửa tay từng video.
5. Không dán mật khẩu, API key, thông tin thẻ, link affiliate có mã bí mật vào chat công khai.

## 8. Dây chuyền tự động hằng ngày — bán tự động (Q10)

**Trả lời ngắn:** AI tự làm video mỗi ngày **được**, nhưng ở mức **bán tự động**. AI chạy theo lịch mọi bước không cần phán đoán. Người giữ 3 việc: **test & quay màn hình**, **Cổng 1**, **Cổng 2 + bấm đăng**. Số liệu ở sheet **NangSuat** (mục Bán tự động) và **ChiPhiVideo** mục F.

### Vì sao không tự động 100%

| Lý do | Hệ quả |
|---|---|
| FTC 16 CFR Part 465: review phải dựa trên trải nghiệm thật | Người phải dùng thử, quay màn hình, viết ghi chú test |
| YouTube không trả tiền cho nội dung sản xuất hàng loạt, lặp lại ("inauthentic content") | Mỗi video cần người duyệt góc nhìn và dữ liệu riêng |
| YouTube Data API: video tải lên từ dự án API **chưa qua kiểm duyệt (audit)** bị khoá ở chế độ riêng tư | Dây chuyền tải lên riêng tư; người hẹn giờ/công khai trong YouTube Studio |
| Flow (Veo trong gói Ultra) **không có API**; Veo qua Gemini API đắt **~9,8 lần** credit gói Ultra (cấp Tiêu chuẩn) | Bước tạo cảnh Veo vẫn làm tay trong Flow, Claude soạn sẵn prompt |
| Kênh B phụ thuộc ý kiến luật sư | Không nối Kênh B vào dây chuyền đăng tự động |

### Một ngày vận hành

```
BAN NGÀY (người)                          BUỔI TỐI (máy, chạy theo lịch)
1. Duyệt danh sách sản phẩm Claude chọn   →  Claude: kịch bản + shot list + bản đọc + tự QC (skill)
2. Test & quay màn hình, ghi chú test     →  ElevenLabs API: giọng đọc
3. Cổng 1: duyệt kịch bản                 →  HeyGen API: người dẫn AI (chỉ Kênh A)
4. Dán prompt Claude soạn vào Flow (Veo)  →  ffmpeg: ráp bản thô theo shot list + phụ đề + template đồ hoạ
                                          →  cat_short.py: 5 short · Claude: gói SEO (skill)
SÁNG HÔM SAU (người)                      →  YouTube Data API: tải lên chế độ RIÊNG TƯ, gửi thông báo
5. Sửa bản thô + Cổng 2 → hẹn giờ trong YouTube Studio
```

### Thời gian người & chi phí (thành thạo, gói B)

| | Hiện tại | Bán tự động |
|---|---|---|
| Phút người / video dài (+ cắt short) | 234 + 25 | **~122 + 10** ⚠️ ước tính |
| Năng lực máy: video dài / ngày / người | 1,6 | ~3,2 (số đăng thật vẫn theo trần đăng & thời gian test) |
| Giờ tiết kiệm / tháng (12 A + 8 B) | — | **~41 giờ** ≈ 3,97 triệu ₫ giờ công |
| Chi phí tăng thêm / tháng | — | **+US$55 ≈ 1,46 triệu ₫** (Claude API US$3/video, gồm dự phòng) → gói B ~21,6 triệu ₫ |
| Giá 1 giờ tiết kiệm | — | **~36 nghìn ₫** (HeyGen Video Agent: 0,57–1,34 triệu ₫) |
| Chi phí xây (một lần) | — | ~30 giờ ≈ 2,9 triệu ₫ giờ công → hoàn vốn **~1,2 tháng** |

⚠️ Giá HeyGen API chưa xác minh: API tính tiền riêng (ví API), không trừ credit gói web. Bảng tính tạm coi bằng giá gói web (ô ThongSo!B60). Nếu chạy phần Claude bằng Claude Code theo lịch trong gói Max thì tiền Claude API gần như 0 (ô ThongSo!B57).

### Lộ trình xây (sau ngày ra mắt 22/10)

| Giai đoạn | Thời gian | Tự động hoá | Xong khi |
|---|---|---|---|
| **GĐ1 — phần chữ** | 23/10–05/11 | Lịch chạy hằng tối: chọn sản phẩm → kịch bản + shot list + bản đọc → tự QC → gói SEO → 5 short (`cat_short.py`); kết quả vào thư mục video trên Drive | 5 video liên tiếp qua Cổng 1 không phải viết lại kịch bản |
| **GĐ2 — phần hình** | 06/11–22/11 | ElevenLabs API, HeyGen API, ráp bản thô bằng ffmpeg theo shot list, tải lên YouTube chế độ riêng tư, thông báo | 5 video liên tiếp qua Cổng 2 với ≤ 45 phút sửa bản thô |
| **GĐ3 — tuỳ chọn** | Sau ngày 60 (22/12) | Short native, nối Kênh B (nếu luật sư đồng ý), xin YouTube kiểm duyệt API | Theo KPI ngày 60 |

### Quy tắc an toàn

1. **Không bao giờ tự công khai** — người bấm hẹn giờ sau Cổng 2.
2. API key lưu trong biến môi trường / quản lý bí mật của máy chạy, **không ghi vào repo** (CLAUDE.md).
3. Đặt **trần chi tiêu API theo ngày** (ElevenLabs, HeyGen, Claude); dây chuyền dừng và báo khi vượt.
4. Bước nào lỗi thì dừng video đó, ghi log, không chạy tiếp các bước sau.
5. Dây chuyền chỉ đọc ghi chú test do người viết. Không có ghi chú test thì **không tạo kịch bản**.
