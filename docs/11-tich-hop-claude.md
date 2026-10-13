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
