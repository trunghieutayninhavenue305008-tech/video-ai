# CLAUDE.md — Xưởng Video AI

Repo này là hồ sơ vận hành của một kênh YouTube tiếng Anh 100% AI (thị trường Global, ngách Lịch sử & Bí ẩn). Đội ngũ là người Việt: **trao đổi, giải thích, ghi chú bằng tiếng Việt; nội dung xuất bản (kịch bản, tiêu đề, caption) bằng tiếng Anh Mỹ.**

## Cấu trúc
- `docs/` — kế hoạch (01 tóm tắt → 12 kịch bản thuyết trình). Số liệu phải khớp với bảng tính.
- `ke-hoach/bang-tinh-ngan-sach-va-van-hanh.xlsx` — nguồn sự thật cho mọi con số (ngân sách, năng suất, hoà vốn, YPP). Khi đổi số trong docs, đổi trong bảng tính trước.
- `templates/` — Bible kênh, brief, checklist QC (mã lỗi K/V/P/S, L1–L20), thư viện prompt.
- `.claude/skills/` — `kich-ban-video`, `qc-video`, `seo-xuat-ban`. Đầu ra của skill phải giữ đúng định dạng vì được đưa thẳng vào sản xuất.
- `tools/cat_short.py` — cắt short bằng Claude API + ffmpeg. Kiểm thử: `python -m unittest tools/test_cat_short.py -v`.

## Quy tắc
- Bible kênh (`templates/kenh-bible.md`) là chuẩn cho giọng văn, phong cách hình, từ cấm, phát âm. Lỗi lặp lại ≥ 2 lần → sửa ở Bible/skill/template, ghi vào mục "Nhật ký thay đổi" của Bible.
- Không tạo nội dung thuộc vùng cấm: tài chính/y tế/pháp lý qua nhân vật AI, tin tức nóng, deepfake người thật, thao túng cảm xúc (xem `docs/09`).
- Không bịa nguồn; điều chưa chắc ghi rõ.
- Không ghi API key, mật khẩu vào file trong repo.
