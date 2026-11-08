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
    table.style = 'Table Grid'
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
        if line_stripped.startswith('|') and line_stripped.endswith('|'):
            if re.match(r'^\|[\s\-\|:]+\|$', line_stripped):
                continue
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
        
        # Đã thay đổi cách khai báo biến chuỗi để tránh lỗi SyntaxError
        if khoi_lop == "Khối 12":
            matrix_rule = (
                "Cấu trúc ĐẶC BIỆT CHO KHỐI 12 (BẮT BUỘC 14 CỘT):\n"
                "- Bảng 1 - MA TRẬN KHUNG (14 cột): (1) TT | (2) Chương/chủ đề | (3) Nội dung/đơn vị kiến thức | (4-6) TN Nhiều lựa chọn (Biết, Hiểu, Vận dụng) | (7-9) TN Đúng-Sai (Biết, Hiểu, Vận dụng) | (10-12) Trả lời ngắn (Biết, Hiểu, Vận dụng) | (13) Tổng số lệnh hỏi | (14) Tỉ lệ % điểm.\n"
                "- Bảng 2 - ĐẶC TẢ CHI TIẾT (14 cột): (1) TT | (2) Chương/chủ đề | (3) Nội dung/đơn vị kiến thức | (4) Yêu cầu cần đạt | (5) Câu | (6-8) TN Nhiều lựa chọn (Biết, Hiểu, VD) | (9-11) TN Đúng-Sai (Biết, Hiểu, VD) | (12-14) Trả lời ngắn (Biết, Hiểu, VD)."
            )
        else:
            matrix_rule = (
                "Cấu trúc ĐẶC BIỆT CHO KHỐI 6, 7, 8, 9, 10, 11 (BẮT BUỘC 14 CỘT - CÓ PHẦN TỰ LUẬN):\n"
                "- Bảng 1 - MA TRẬN KHUNG (14 cột): (1) TT | (2) Chương/chủ đề | (3) Nội dung/đơn vị kiến thức | (4-6) TN Nhiều lựa chọn (Biết, Hiểu, VD) | (7-9) TN Đúng-Sai (Biết, Hiểu, VD) | (10-12) Tự luận (Biết, Hiểu, VD) | (13) Tổng số câu | (14) Tỉ lệ % điểm.\n"
                "- Bảng 2 - ĐẶC TẢ CHI TIẾT (14 cột): (1) TT | (2) Chương/chủ đề | (3) Nội dung/đơn vị kiến thức | (4) Yêu cầu cần đạt | (5) Câu | (6-8) TN Nhiều lựa chọn (Biết, Hiểu, VD) | (9-11) TN Đúng-Sai (Biết, Hiểu, VD) | (12-14) Tự luận (Biết, Hiểu, VD)."
            )
            
        system_instruction = f"""
        Bạn là chuyên gia sư phạm Toán học. Hãy đọc đề thi được cung cấp và trích xuất trọn bộ 5 hạng mục độc lập. 
        ĐỂ HỆ THỐNG CÓ THỂ TÁCH THÀNH 5 FILE WORD, BẮT BUỘC PHẢI ĐẶT NỘI DUNG TỪNG HẠNG MỤC VÀO GIỮA CÁC THẺ TAG SAU:

        [START_MATRAN]
        (Nội dung Ma trận khung - BẮT BUỘC KẺ BẢNG MARKDOWN)
        [END_MATRAN]

        [START_DACTA]
        (Nội dung Bản đặc tả chi tiết - BẮT BUỘC KẺ BẢNG MARKDOWN)
        [END_DACTA]

        [START_DETHI]
        (Nội dung Đề thi hoàn chỉnh đã gán mã năng lực và mức độ, vd: Nhận biết - TD1.1)
        [END_DETHI]

        [START_DAPAN]
        (Nội dung Bảng đáp án chi tiết - BẮT BUỘC KẺ BẢNG MARKDOWN)
        [END_DAPAN]

        [START_LOIGIAI]
        (Nội dung Lời giải chi tiết và Thang điểm chấm - BẮT BUỘC KẺ BẢNG MARKDOWN cho thang điểm)
        [END_LOIGIAI]
        
        QUY TẮC ĐỊNH DẠNG NGHIÊM NGẶT:
        - {matrix_rule}
        - Mọi công thức toán học, biểu thức, ký hiệu góc phải kẹp trong cặp dấu $ ... $ (chuẩn LaTeX inline). Tuyệt đối không dùng \\( ... \\).
        - Mọi bảng biến thiên, bảng xét dấu, đồ thị, hình học không gian BẮT BUỘC viết bằng mã TikZ trong môi trường \\begin{{tikzpicture}} ... \\end{{tikzpicture}}.
        """
        
        model = genai.GenerativeModel(model_name='gemini-1.5-flash', system_instruction=system_instruction)
        
        with st.spinner("Hệ thống QTOAN đang xử lý, dựng bảng Word và tách 5 file độc lập... Vui lòng đợi..."):
            if uploaded_file.name.endswith(".txt"):
                content = uploaded_file.getvalue().decode("utf-8")
            else:
                doc_reader = docx.Document(uploaded_file)
                content = "\n".join([para.text for para in doc_reader.paragraphs])
                
            try:
                response = model.generate_content(content)
                
                matran = extract_section(response.text, "[START_MATRAN]", "[END_MATRAN]")
                dacta = extract_section(response.text, "[START_DACTA]", "[END_DACTA]")
                dethi = extract_section(response.text, "[START_DETHI]", "[END_DETHI]")
                dapan = extract_section(response.text, "[START_DAPAN]", "[END_DAPAN]")
                loigiai = extract_section(response.text, "[START_LOIGIAI]", "[END_LOIGIAI]")
                
                f_matran = create_docx(matran)
                f_dacta = create_docx(dacta)
                f_dethi = create_docx(dethi)
                f_dapan = create_docx(dapan)
                f_loigiai = create_docx(loigiai)
                
                st.success("✅ Đã phân tích và tạo thành công 5 file Word chuẩn!")
                
                zip_buffer = BytesIO()
                with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
                    zip_file.writestr(f"1_Ma_tran_khung_{khoi_lop}.docx", f_matran)
                    zip_file.writestr(f"2_Ban_dac_ta_{khoi_lop}.docx", f_dacta)
                    zip_file.writestr(f"3_De_thi_{khoi_lop}.docx", f_dethi)
                    zip_file.writestr(f"4_Dap_an_{khoi_lop}.docx", f_dapan)
                    zip_file.writestr(f"5_Loi_giai_Thang_diem_{khoi_lop}.docx", f_loigiai)
                
                st.download_button(
                    label="📦 TẢI VỀ TRỌN BỘ 5 FILE (ĐÓNG GÓI .ZIP)",
                    data=zip_buffer.getvalue(),
                    file_name=f"QTOAN_Tron_bo_5_File_{khoi_lop}.zip",
                    mime="application/zip",
                    use_container_width=True
                )
                
                st.markdown("### Hoặc tải từng file Word độc lập:")
                col1, col2, col3, col4, col5 = st.columns(5)
                col1.download_button("📥 1. Ma trận", f_matran, f"1_Ma_tran_khung_{khoi_lop}.docx")
                col2.download_button("📥 2. Đặc tả", f_dacta, f"2_Ban_dac_ta_{khoi_lop}.docx")
                col3.download_button("📥 3. Đề thi", f_dethi, f"3_De_thi_{khoi_lop}.docx")
                col4.download_button("📥 4. Đáp án", f_dapan, f"4_Dap_an_{khoi_lop}.docx")
                col5.download_button("📥 5. Lời giải", f_loigiai, f"5_Loi_giai_Thang_diem_{khoi_lop}.docx")
                
            except Exception as e:
                st.error(f"Lỗi hệ thống: {e}")
