import streamlit as st
import google.generativeai as genai
import docx
from io import BytesIO
import re
import zipfile

# --- THUẬT TOÁN HỖ TRỢ VẼ BẢNG, KHUNG VIỀN TỰ ĐỘNG VÀO WORD ---
def render_table(doc, data):
    if not data: return
    cols = max(len(row) for row in data)
    table = doc.add_table(rows=len(data), cols=cols)
    table.style = 'Table Grid' # Lệnh này tạo khung, viền đen chuẩn của Word
    for r, row_data in enumerate(data):
        for c, cell_text in enumerate(row_data):
            if c < cols:
                table.cell(r, c).text = cell_text

def add_markdown_to_doc(doc, text):
    lines = text.split('\n')
    in_table = False
    table_data = []
    for line in lines:
        line_stripped = line.strip()
        # Nếu dòng có định dạng bảng Markdown
        if line_stripped.startswith('|') and line_stripped.endswith('|'):
            if re.match(r'^\|[\s\-\|:]+\|$', line_stripped):
                continue # Bỏ qua dòng kẻ ngang của Markdown (---|---)
            cells = [cell.strip() for cell in line_stripped.strip('|').split('|')]
            table_data.append(cells)
            in_table = True
        else:
            if in_table:
                render_table(doc, table_data)
                table_data = []
                in_table = False
            doc.add_paragraph(line)
    if in_table:
        render_table(doc, table_data)

def extract_section(text, start_tag, end_tag):
    pattern = re.escape(start_tag) + r"(.*?)" + re.escape(end_tag)
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else f"Lỗi: Không tìm thấy nội dung cho phần {start_tag}. Vui lòng thử khởi tạo lại."

def create_docx(text):
    doc = docx.Document()
    add_markdown_to_doc(doc, text)
    bio = BytesIO()
    doc.save(bio)
    return bio.getvalue()

# --- GIAO DIỆN CHÍNH ---
st.set_page_config(page_title="Hệ thống Ma trận & Đề thi - QTOAN Tools", layout="wide")
st.title("Hệ thống Tự động Phân tích Đề & Lập Ma Trận Toán Học")

with st.sidebar:
    st.header("Cấu hình hệ thống")
    api_key = st.text_input("Nhập Google Gemini API Key:", type="password")
    khoi_lop = st.radio("Chọn khối lớp:", ["Khối 6, 7, 8, 9, 10, 11", "Khối 12"])
    st.markdown("---")
    st.info("Định dạng bắt buộc:\n- Công thức: `$ ... $`\n- Hình vẽ: `TikZ`\n- File xuất: 5 file Word độc lập có bảng biểu.")

uploaded_file = st.file_uploader("Đưa đề thi gốc vào đây (định dạng .txt hoặc Word)", type=["txt", "docx"])

if st.button("Khởi tạo Trọn Bộ (Xuất 5 File Word)"):
    if not api_key:
        st.warning("⚠️ Thầy ơi, hãy nhập API Key vào ô trống ở thanh bên trái (Sidebar) trước khi bấm khởi tạo nhé!")
    elif not uploaded_file:
        st.warning("⚠️ Thầy chưa tải file đề thi lên!")
    else:
        genai.configure(api_key=api_key)
        
        if khoi_lop == "Khối 12":
            matrix_rule = """Cấu trúc ĐẶC BIỆT CHO KHỐI 12 (BẮT BUỘC 14 CỘT):
            - Bảng 1 - MA TRẬN KHUNG (14 cột): (1) TT | (2) Chương/chủ đề | (3) Nội dung/đơn vị kiến thức | (4-6) TN Nhiều lựa chọn (Biết, Hiểu, Vận dụng) | (7-9) TN Đúng-Sai (Biết, Hiểu, Vận dụng) | (10-12) Trả lời ngắn (Biết, Hiểu, Vận dụng) | (13) Tổng số lệnh hỏi | (14) Tỉ lệ % điểm.
            - Bảng 2 - ĐẶC TẢ CHI TIẾT (14 cột): (1) TT | (2) Chương/chủ đề | (3) Nội dung/đơn vị kiến thức | (4) Yêu cầu cần đạt | (5) Câu | (6-8) TN Nhiều lựa chọn (Biết, Hiểu, VD) | (9-11) TN Đúng-Sai (Biết, Hiểu, VD) | (12-14) Trả lời ngắn (Biết, Hiểu, VD)."""
        else:
            matrix_rule = """Cấu trúc ĐẶC BIỆT CHO KHỐI 6, 7, 8, 9, 10, 11 (BẮT BUỘC 14 CỘT - CÓ PHẦN TỰ LUẬN):
            - Bảng 1 - MA TRẬN KHUNG (14 cột): (1) TT | (2) Chương/chủ đề | (3) Nội dung/đơn vị kiến thức | (4-6) TN Nhiều lựa chọn (Biết, Hiểu, VD) | (7-9) TN Đúng-Sai (Biết, Hiểu, VD) | (10-12) Tự luận (Biết, Hiểu, VD) | (13) Tổng số câu | (14) Tỉ lệ % điểm.
            - Bảng 2 - ĐẶC TẢ CHI TIẾT (14 cột): (1) TT | (2) Chương/chủ đề | (3) Nội dung/đơn vị kiến thức | (4) Y
