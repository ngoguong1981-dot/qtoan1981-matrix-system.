import pandas as pd
import streamlit as st
import google.generativeai as genai
import docx
from io import BytesIO

# Cấu hình trang
st.set_page_config(page_title="Hệ thống Ma trận & Đề thi - QTOAN Tools", layout="wide")
st.title("Hệ thống Tự động Phân tích Đề & Lập Ma Trận Toán Học")

# Hàm xử lý file Excel Ma Trận
def process_matrix_excel(uploaded_file):
    try:
        excel_file = pd.ExcelFile(uploaded_file)
        matrix_text = "CẤU TRÚC MA TRẬN VÀ ĐẶC TẢ TỪ FILE EXCEL:\n\n"
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
            df = df.dropna(how='all').dropna(axis=1, how='all')
            df = df.ffill(axis=0) # Điền ô gộp
            matrix_text += f"--- Sheet: {sheet_name} ---\n"
            matrix_text += df.to_markdown(index=False) + "\n\n"
        return matrix_text
    except Exception as e:
        return f"Lỗi đọc Excel: {str(e)}"

# Hàm đọc file Word (hỗ trợ đọc cả bảng biểu)
def read_word_file(file):
    doc = docx.Document(file)
    content = []
    for para in doc.paragraphs:
        if para.text.strip():
            content.append(para.text)
    for table in doc.tables:
        for row in table.rows:
            row_data = [cell.text.strip() for cell in row.cells if cell.text.strip()]
            if row_data:
                content.append(" | ".join(row_data))
    return "\n".join(content)

with st.sidebar:
    st.header("Cấu hình hệ thống")
    
    # Tạo giao diện nhập API Key trực tiếp
    api_key = st.text_input("Nhập Google Gemini API Key:", type="password", help="Lấy khóa tại aistudio.google.com/app/apikey")
    if not api_key:
        st.warning("⚠️ Vui lòng nhập API Key để sử dụng hệ thống.")

    khoi_lop = st.radio("Chọn khối lớp:", ["Khối 6-11", "Khối 12"])
    st.markdown("---")
    
    st.subheader("Cấu hình Ma trận")
    matrix_file = st.file_uploader("Tải lên cấu trúc (Excel .xlsx)", type=["xlsx"])
    matrix_context = ""
    if matrix_file is not None:
        matrix_context = process_matrix_excel(matrix_file)
        st.success("Đã nạp cấu trúc Ma trận!")

    st.markdown("---")
    st.info("Định dạng bắt buộc:\n- Công thức: `$ ... $`\n- Hình vẽ: `TikZ`")
    st.markdown("**Bản quyền:** thầy Quang Toàn-dạy toán-0387997970")

uploaded_file = st.file_uploader("Đưa đề thi gốc vào đây (định dạng .txt hoặc Word)", type=["txt", "docx"])

if st.button("Khởi tạo Trọn Bộ (5 Hạng Mục)") and uploaded_file and api_key:
    genai.configure(api_key=api_key)
    
    if khoi_lop == "Khối 12":
        matrix_rule = "Áp dụng cấu trúc Ma trận khung và Đặc tả 14 cột chuẩn môn Toán 12 (TNKQ 4 phương án, TN Đúng/Sai, TN Trả lời ngắn)."
    else:
        matrix_rule = "Áp dụng cấu trúc Ma trận khung và Đặc tả 15 cột chuẩn môn Toán (TNKQ 4 phương án, TN Đúng/Sai, Tự luận/Trả lời ngắn)."
        
    system_instruction = f"""
    Bạn là chuyên gia sư phạm Toán học. Hãy đọc đề thi được cung cấp và trích xuất trọn bộ 5 hạng mục:
    1. Ma trận khung.
    2. Bản đặc tả chi tiết.
    3. Đề thi hoàn chỉnh đã gán mã năng lực và mức độ (Ví dụ: Nhận biết - TD1.1).
    4. Bảng đáp án chi tiết.
    5. Lời giải chi tiết.
    
    {matrix_context}
    
    QUY TẮC ĐỊNH DẠNG:
    - {matrix_rule}
    - Mọi công thức toán học phải bọc trong $ ... $. Tuyệt đối không dùng \( ... \).
    - Mọi hình vẽ, đồ thị, bảng biến thiên BẮT BUỘC vẽ bằng mã TikZ trong môi trường \\begin{{tikzpicture}} ... \\end{{tikzpicture}}.
    """
    
    # Sử dụng tên model chuẩn gemini-1.5-pro tương thích hoàn hảo với mọi dạng API Key Google Cloud
    model = genai.GenerativeModel(model_name='gemini-1.5-pro', system_instruction=system_instruction)
    
    # Xử lý file đề thi gốc
    if uploaded_file.name.endswith(".txt"):
        exam_content = uploaded_file.getvalue().decode("utf-8")
    else:
        exam_content = read_word_file(uploaded_file)
        
    # Tạo hiệu ứng streaming text cho UX mượt mà
    response_placeholder = st.empty()
    full_response = ""
    
    with st.spinner("Hệ thống QTOAN đang xử lý, phân tích mã năng lực và vẽ TikZ..."):
        try:
            response = model.generate_content(exam_content, stream=True)
            for chunk in response:
                full_response += chunk.text
                response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)
            
            doc_out = docx.Document()
            doc_out.add_paragraph(full_response)
            bio = BytesIO()
            doc_out.save(bio)
            
            st.success("✅ Đã khởi tạo thành công 5 hạng mục!")
            st.download_button(
                label="📥 Tải trọn bộ tài liệu (.docx)",
                data=bio.getvalue(),
                file_name=f"Tron_bo_Ma_tran_De_thi_{khoi_lop}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        except Exception as e:
            st.error(f"Lỗi hệ thống: {e}")
