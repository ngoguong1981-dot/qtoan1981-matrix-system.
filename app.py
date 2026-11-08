import streamlit as st
import google.generativeai as genai
import docx
from io import BytesIO

st.set_page_config(page_title="Hệ thống Ma trận & Đề thi - QTOAN Tools", layout="wide")
st.title("Hệ thống Tự động Phân tích Đề & Lập Ma Trận Toán Học")

with st.sidebar:
    st.header("Cấu hình hệ thống")
    # Thay vì dùng st.secrets, tạo ô nhập API Key trực tiếp trên giao diện để tránh mọi lỗi cấu hình
    api_key = st.text_input("Nhập Google Gemini API Key:", type="password")
    khoi_lop = st.radio("Chọn khối lớp:", ["Khối 6, 7, 8, 9, 10, 11", "Khối 12"])
    st.markdown("---")
    st.info("Định dạng bắt buộc:\n- Công thức: `$ ... $`\n- Hình vẽ: `TikZ`")

uploaded_file = st.file_uploader("Đưa đề thi gốc vào đây (định dạng .txt hoặc Word)", type=["txt", "docx"])

if st.button("Khởi tạo Trọn Bộ (5 Hạng Mục)"):
    if not api_key:
        st.warning("AQ.Ab8RN6Li-R8pvQ9s9hwFcZEHXEKG1PsV7zjJaDlZceDPCTrzRg")
    elif not uploaded_file:
        st.warning("AQ.Ab8RN6Li-R8pvQ9s9hwFcZEHXEKG1PsV7zjJaDlZceDPCTrzRg")
    else:
        genai.configure(api_key=api_key)
        
        if khoi_lop == "Khối 12":
            matrix_rule = "Áp dụng cấu trúc Ma trận khung và Đặc tả 14 cột chuẩn môn Toán 12 (TNKQ 4 phương án, TN Đúng/Sai, TN Trả lời ngắn)."
        else:
            matrix_rule = "Áp dụng cấu trúc Ma trận khung và Đặc tả 15 cột chuẩn môn Toán 11 (TNKQ 4 phương án, TN Đúng/Sai, Tự luận/Trả lời ngắn)."
            
        system_instruction = f"""
        Bạn là chuyên gia sư phạm Toán học. Hãy đọc đề thi được cung cấp và trích xuất trọn bộ 5 hạng mục sau:
        1. Ma trận khung.
        2. Bản đặc tả chi tiết.
        3. Đề thi hoàn chỉnh đã gán mã năng lực và mức độ (Ví dụ: Nhận biết - TD1.1) vào đầu mỗi câu/mỗi ý a,b,c,d.
        4. Bảng đáp án chi tiết.
        5. Lời giải chi tiết.
        
        QUY TẮC ĐỊNH DẠNG NGHIÊM NGẶT:
        - {matrix_rule}
        - Mọi công thức toán học, biểu thức, ký hiệu góc phải được kẹp trong cặp dấu $ ... $ (chuẩn LaTeX inline) để tương thích MathType. Tuyệt đối không dùng \\( ... \\).
        - Mọi bảng biến thiên, bảng xét dấu, đồ thị hàm số và hình vẽ hình học (phẳng & không gian) BẮT BUỘC phải viết bằng mã TikZ (kết hợp tkz-tab, tkz-euclide, pgfplots). Bọc mã trong môi trường \\begin{{tikzpicture}} ... \\end{{tikzpicture}}.
        """
        
        model = genai.GenerativeModel(model_name='gemini-2.5-flash', system_instruction=system_instruction)
        
        with st.spinner("Hệ thống QTOAN đang xử lý, phân tích mã năng lực và vẽ TikZ... Vui lòng đợi..."):
            if uploaded_file.name.endswith(".txt"):
                content = uploaded_file.getvalue().decode("utf-8")
            else:
                doc_reader = docx.Document(uploaded_file)
                content = "\n".join([para.text for para in doc_reader.paragraphs])
                
            try:
                response = model.generate_content(content)
                st.success("✅ Đã khởi tạo thành công 5 hạng mục!")
                
                doc_out = docx.Document()
                doc_out.add_paragraph(response.text)
                bio = BytesIO()
                doc_out.save(bio)
                
                st.download_button(
                    label="📥 Tải trọn bộ tài liệu (.docx)",
                    data=bio.getvalue(),
                    file_name=f"Tron_bo_Ma_tran_De_thi_{khoi_lop}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            except Exception as e:
                st.error(f"Lỗi khi kết nối API: {e}")
