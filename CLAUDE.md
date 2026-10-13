# CLAUDE.md — Xưởng Video AI (kênh review)

Repo này là hồ sơ vận hành của 2 kênh YouTube tiếng Anh sản xuất bằng AI cho thị trường Global:
- **Kênh A — Tech & AI Tools:** review SaaS, AI tool, sản phẩm vật lý công nghệ. Có người dẫn AI trông như người thật.
- **Kênh B — Crypto & Forex:** review sàn và broker. **Không người dẫn AI**, chỉ đăng khi có ý kiến luật sư.

Đội ngũ là người Việt: **trao đổi, giải thích, ghi chú bằng tiếng Việt; nội dung xuất bản (kịch bản, tiêu đề, caption) bằng tiếng Anh Mỹ.**

## Cấu trúc
- `docs/`: kế hoạch (01 tóm tắt → 12 kịch bản thuyết trình). Số liệu phải khớp với bảng tính.
- `ke-hoach/bang-tinh-ngan-sach-va-van-hanh.xlsx`: nguồn sự thật cho mọi con số (ngân sách, credit, năng suất, affiliate, hoà vốn, YPP). Khi đổi số trong docs, đổi trong bảng tính trước.
- `templates/`:
  - Bible 2 kênh: người dẫn AI, câu công khai và cảnh báo chuẩn.
  - Brief có ghi chú test.
  - Checklist QC: mã K/C/V/P/S, L1–L25.
  - Thư viện prompt.
- `.claude/skills/`: `kich-ban-video`, `qc-video`, `seo-xuat-ban`. Đầu ra của skill phải giữ đúng định dạng vì được đưa thẳng vào sản xuất.
- `tools/cat_short.py`: cắt short bằng Claude API + ffmpeg. Tuỳ chọn `--note` thêm dòng cảnh báo. Kiểm thử bằng lệnh `python -m unittest tools/test_cat_short.py -v`.

## Quy tắc
- **Chỉ khẳng định điều có trong ghi chú test hoặc nguồn chính thức (link + ngày).** Không bịa trải nghiệm, số liệu, lời chứng thực (FTC 16 CFR Part 465).
- **Công khai 3 lớp:**
  - Câu affiliate bằng lời trong 30 giây đầu.
  - Chữ trên hình.
  - Dòng đầu mô tả.
- Kênh A thêm chữ "AI-generated presenter" và luôn bật nhãn "Altered or synthetic content".
- **Kênh B:**
  - Không vai HOST, không nhân vật AI.
  - Không lời khuyên đầu tư, không hứa lợi nhuận.
  - Có cảnh báo rủi ro ở đầu, ở cuối và trên mọi short.
  - Chỉ sàn/broker có giấy phép cấp 1.
  - Có lọc quốc gia, không nội dung tiếng Việt.
- Bible (`templates/kenh-bible.md`) là chuẩn cho giọng văn, hình, từ cấm, phát âm. Lỗi lặp lại ≥ 2 lần → sửa ở Bible/skill/template, ghi vào "Nhật ký thay đổi" của Bible.
- Không deepfake người thật; người dẫn AI là nhân vật hư cấu.
- Không bịa nguồn; điều chưa chắc ghi rõ (⚠️).
- Không ghi API key, mật khẩu, mã affiliate bí mật vào file trong repo.
