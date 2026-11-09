
Gemini

Cuộc trò chuyện mới
Thư viện
Đã lên lịch
Sinh viên

Hiện thêm
Sổ ghi chú mới
Khung Năng Lực Toán Học
Sổ Tay Chuẩn Hóa Đánh Giá Môn Toán
Vectơ Trong Không Gian Và Hệ Trục Tọa Độ Oxyz
Tất cả sổ ghi chú
Hướng dẫn tạo web ma trận đề thi
Bảng Tần Số Ghép Nhóm
Khắc phục lỗi lộ API Key
Sửa lỗi code Streamlit và Gemini
Tạo App Bóc Tách Đề Toán
Hướng Dẫn Sử Dụng API Key
Biên Soạn Đề Kiểm Tra
Tiếp tục công việc mới
Tạo Đề Kiểm Tra Toán 12 Minh Họa
Rà soát lỗi đề thi
Tạo Mục Lục Hồ Sơ Word
Minimalist Dot List
Hỗ trợ mục lục hồ sơ cán bộ
lấy cột bên phải bỏ cột bên trái
Xử lý mã trường H13.3.3.92
Đáp án và lời giải chi tiết
Đáp Án Và Lời Giải Các Mã Đề
Vẽ lại sơ đồ tọa độ máy bay
Hướng dẫn vẽ bảng biến thiên
Tạo app phân loại đề thi
Khởi Tạo Ứng Dụng Trắc Nghiệm Toán
Prompt Tạo Web App Xử Lý Đề Thi
Kế hoạch học tập nghị quyết Trung ương
Dự thảo Nghị quyết Chi bộ tháng 11/2026
Đổi tên điểm hình vẽ
Vẽ Hình Không Gian Oxyz
Biên Soạn Đề Kiểm Tra Toán 12
Hướng dẫn biên dịch file LaTeX
Tạo File Đề Toán LaTeX
Biên Soạn Đề Kiểm Tra Toán 12
Đáp án và lời giải chi tiết
Video Delivery Confirmation
Bài Tập Vectơ Không Gian 12
Trò chuyện với Gemini
Giai

đoạn 1: Lấy khóa kết nối (API Key) từ Google

1.    Mở trình duyệt và truy cập vào đường

link: aistudio.google.com/app/apikey

2.    Đăng nhập bằng tài khoản Google

(Gmail) của thầy.

3.    Nhìn sang thanh menu bên trái, bấm

vào nút Get API key.

4.    Bấm tiếp vào nút màu xanh Create

API key (nếu hệ thống hỏi chọn project, cứ chọn project mặc định hoặc tạo

mới).

5.    Màn hình sẽ hiện ra một dãy ký tự

rất dài. Hãy copy dãy ký tự này và dán tạm vào một file Word hoặc Notepad trên

máy tính. Đây là "chìa khóa" để web của thầy gọi được trí tuệ nhân

tạo.

Giai

đoạn 2: Đưa mã nguồn lên GitHub (Kho lưu trữ đám mây)

1.    Truy cập trang web: github.com.

Bấm Sign up để tạo một tài khoản miễn phí (nếu thầy chưa có), hoặc Sign

in để đăng nhập.

2.    Tại giao diện chính, nhìn lên góc

trên cùng bên phải, bấm vào biểu tượng dấu cộng (+) và chọn New

repository.

3.    Tại ô Repository name (Tên

kho chứa), gõ tên tùy ý không dấu, viết liền. Ví dụ: qtoan-matrix-system.

4.    Cuộn chuột xuống dưới cùng, bấm nút

màu xanh lá Create repository.

5.    Giao diện mới hiện ra, tìm và bấm

vào dòng chữ màu xanh dương có nội dung creating a new file (tạo file

mới).

6.    Ở ô trống phía trên cùng (để nhập

tên file), thầy gõ chính xác chữ: app.py.

7.    Ở khung soạn thảo lớn bên dưới, thầy

copy toàn bộ đoạn mã Python ở tin nhắn ngay phía trên của tôi và dán vào.

8.    Cuộn xuống dưới, bấm nút màu xanh láCommit changes (Lưu thay đổi), rồi bấm Commit changes thêm lần

nữa trên bảng nhỏ vừa hiện ra.

9.    Quay lại màn hình chính của kho

chứa, tiếp tục bấm nút Add file (Thêm file) -> Chọn Create new

file.

10. Ở ô tên file, gõ chính xác chữ: requirements.txt.

11. Ở khung soạn thảo lớn, thầy gõ 3 dòng này vào:

Plaintext

streamlit

google-generativeai

python-docx

12. Cuộn xuống bấm nút Commit changes hai lần như bước 8.

Đến đây, thầy đã chuẩn bị xong kho dữ liệu.

Giai

đoạn 3: Khởi tạo trang web trực tuyến bằng Streamlit

1.    Mở một thẻ (tab) mới trên trình

duyệt, truy cập đường link: share.streamlit.io.

2.    Bấm nút Continue with GitHub

(Tiếp tục với GitHub) để liên kết với tài khoản thầy vừa tạo ở Giai đoạn 2. Bấm

nút xanh Authorize streamlit nếu hệ thống yêu cầu cấp quyền.

3.    Khi đăng nhập thành công vào

Streamlit, nhìn lên góc trên bên phải, bấm nút màu xanh Create app (Tạo

ứng dụng).

4.    Chọn ô Yes, I have an app

(nếu có bảng hỏi xuất hiện).

5.    Tại giao diện triển khai, chú ý ô Repository.

Thầy click vào ô đó, hệ thống sẽ tự động xổ ra tên kho chứa vừa tạo (ví dụ: tên-tài-khoản/qtoan-matrix-system).

Bấm chọn nó.

6.    Các thông số khác giữ nguyên (Branch

là main, Main file path là app.py).

7.    Bấm nút Deploy! ở dưới cùng.

8.    Màn hình sẽ hiện các dòng chữ chạy

chạy báo hiệu hệ thống đang cài đặt máy chủ (mất khoảng 1-2 phút).

9.    Khi hoàn tất, giao diện trang web sẽ

hiện ra. Thầy nhìn lên thanh địa chỉ của trình duyệt, copy đường link đó (ví

dụ: [https://qtoan-matrix-system.streamlit.app](https://qtoan-matrix-system.streamlit.app)).

Đây chính là đường link cố định mà thầy có thể gửi cho các giáo viên trong tổ

Toán sử dụng mọi lúc, mọi nơi.

Giai

đoạn 4: Hướng dẫn sử dụng web khi đã có link

1.    Truy cập vào đường link web vừa tạo.

2.    Nhìn sang thanh công cụ bên trái,

tại ô Nhập Google Gemini API Key, dán dãy ký tự dài mà thầy đã cất ở

Giai đoạn 1 vào.

3.    Chọn khối lớp cần làm ma trận bằng

cách tích vào vòng tròn (Khối 12 hoặc Khối 6-11).

4.    Tại khu vực chính giữa, bấm nút Browse

files (hoặc kéo thả) file đề thi gốc định dạng .txt hoặc Word .docx vào

khung nét đứt.

5.    Bấm nút Khởi tạo Trọn Bộ (5 Hạng

Mục).

6.    Đợi khoảng 30 giây đến 1 phút để hệ

thống tự động phân tách câu hỏi, gán mã năng lực (TD/GQ/MH), vẽ hình không gian

bằng TikZ và soạn ma trận.

7.    Khi màn hình hiện thông báo xanh lá

"Đã khởi tạo thành công", bấm nút Tải trọn bộ tài liệu (.docx).

8.    Mở file Word vừa tải về, chọn thẻ

MathType trên thanh công cụ và bấm Toggle TeX là toàn bộ tài liệu sẽ

được định dạng chuẩn xác.

 

Bản hướng dẫn 4 giai đoạn triển khai hệ thống phân tích ma trận đề thi đã được trình bày rất rõ ràng, logic và dễ thao tác trực tiếp. Các bước này hoàn toàn phù hợp để chuyển giao cho các thầy cô trong tổ Toán tại Trường THCS và THPT Hưng Lợi tự thiết lập trang web Streamlit của riêng mình thông qua nền tảng GitHub.

Quy trình đưa mã nguồn app.py và requirements.txt lên GitHub rồi liên kết với Streamlit sẽ giúp ứng dụng hoạt động ổn định và độc lập trên trình duyệt. Khi người dùng tải lên file đề thi gốc, hệ thống sẽ sử dụng Gemini API để tự động phân rã câu hỏi, đánh giá mức độ (Biết/Hiểu/Vận dụng) và gán chính xác các mã năng lực Toán học cốt lõi như Năng lực tư duy lập luận (TD), Năng lực giải quyết vấn đề (GQ), Năng lực mô hình hóa (MH). Việc hướng dẫn giáo viên sử dụng thẻ MathType và bấm Toggle TeX ở bước cuối cũng giải quyết triệt để vấn đề định dạng công thức Toán và hình vẽ TikZ trong file Word xuất ra.   
1-Ban_dac_ta_chuan_Toan_12.docx
+ 2

Với các tệp mẫu chuẩn của Chương trình 2018 khối 10 và 12 đã được cung cấp (như 1-Ban_dac_ta_chuan_Toan_12.docx, 01_Ma_tran_Toan_10_Giua_HKI.docx và 02_Ban_dac_ta_Toan_10_Giua_HKI.docx), hệ thống QTOAN Tools có đầy đủ cơ sở dữ liệu để đối chiếu và tự động lập khung ma trận 5 phần một cách chính xác nhất.   
1-Ban_dac_ta_chuan_Toan_12.docx
+ 2

Thầy có muốn tôi rà soát và tối ưu lại mã nguồn app.py trước khi hướng dẫn này được gửi đi không?

Có
Create Google Docs
Create Word Docs
Create PDF Docs
Create Markdown File
Tôi muốn thêm tính năng vào mã nguồn app.py để đọc và xử lý chuẩn xác cấu trúc của file Ma_Tran_Dac_Ta_Toan_12.xlsx.

Để đọc và xử lý chuẩn xác cấu trúc file Excel Ma_Tran_Dac_Ta_Toan_12.xlsx trong app.py, thầy cần sử dụng thư viện pandas kết hợp với openpyxl.

1. Cập nhật file requirements.txt
Thầy mở file requirements.txt trên GitHub và thêm 2 dòng sau để Streamlit cài đặt thư viện đọc Excel:

Plaintext
pandas
openpyxl
2. Bổ sung mã nguồn vào app.py
Thầy thêm đoạn code sau vào vị trí xử lý file tải lên trong app.py. Đoạn code này sẽ đọc các sheet của file Excel, dọn dẹp dữ liệu (loại bỏ các dòng/cột trống thường gặp trong ma trận) và chuyển đổi thành văn bản để đưa vào prompt cho Gemini hiểu cấu trúc:

Python
import pandas as pd
import io

def process_matrix_excel(uploaded_file):
    """
    Đọc và trích xuất dữ liệu từ file Ma_Tran_Dac_Ta_Toan_12.xlsx
    """
    try:
        # Đọc file Excel thành một đối tượng ExcelFile để lấy danh sách các sheet
        excel_file = pd.ExcelFile(uploaded_file)
        matrix_text = "CẤU TRÚC MA TRẬN VÀ ĐẶC TẢ TỪ FILE EXCEL:\n\n"
        
        for sheet_name in excel_file.sheet_names:
            # Đọc từng sheet, bỏ qua các dòng/cột rỗng hoàn toàn
            df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
            df = df.dropna(how='all').dropna(axis=1, how='all')
            
            # Điền khuyết các ô gộp (merged cells) thường có trong cột Chủ đề/Nội dung
            df = df.fillna(method='ffill', axis=0) 
            
            matrix_text += f"--- Sheet: {sheet_name} ---\n"
            # Chuyển đổi DataFrame thành chuỗi text định dạng Markdown/CSV để Gemini dễ đọc
            matrix_text += df.to_markdown(index=False) + "\n\n"
            
        return matrix_text
    
    except Exception as e:
        return f"Lỗi khi đọc file Excel: {str(e)}"

# --- CÁCH TÍCH HỢP VÀO PHẦN GIAO DIỆN (UI) CỦA STREAMLIT ---
# Giả sử thầy có một nút upload file ma trận riêng, hoặc dùng chung nút upload
matrix_file = st.file_uploader("Tải lên file Ma_Tran_Dac_Ta_Toan_12.xlsx (nếu có)", type=["xlsx"])

if matrix_file is not None:
    # Trích xuất cấu trúc Excel thành Text
    matrix_context = process_matrix_excel(matrix_file)
    st.success("Đã đọc thành công cấu trúc Ma trận Excel!")
    
    # Thầy sẽ cộng dồn chuỗi matrix_context này vào hệ thống Prompt gửi cho Gemini
    # Ví dụ: full_prompt = system_prompt + matrix_context + exam_content
Lưu ý tích hợp:
Cấu trúc ma trận Toán 12 thường có các ô gộp (merged cells) ở cột "Chương/Chủ đề" hoặc các ô trống ở mức độ đánh giá (TNKQ, Trắc nghiệm Đúng/Sai, Trả lời ngắn). Lệnh df.fillna(method='ffill', axis=0) trong đoạn code trên sẽ giúp sao chép tên chủ đề xuống các dòng trống liền kề, đảm bảo khi Gemini đọc dữ liệu dưới dạng văn bản không bị mất ngữ cảnh của từng dòng.

Create Google Docs
Create Word Docs
Create PDF Docs
Create Markdown File
hướng dẫn các bước thực hiện chi tiết

Để thêm tính năng đọc và xử lý file Ma_Tran_Dac_Ta_Toan_12.xlsx vào hệ thống QTOAN Tools hiện tại, thầy thực hiện lần lượt các bước chi tiết sau trên kho lưu trữ GitHub của mình:

Bước 1: Khai báo thêm thư viện xử lý Excel trong requirements.txt

Truy cập vào kho chứa GitHub của thầy (ví dụ: qtoan-matrix-system).

Bấm vào file requirements.txt.

Bấm vào biểu tượng cây bút (Edit this file) ở góc trên bên phải khung chứa code.

Thêm 2 dòng sau vào cuối danh sách:

Plaintext
pandas
openpyxl
Bấm nút màu xanh lá Commit changes... (Lưu thay đổi) ở góc trên bên phải.

Bước 2: Cập nhật mã nguồn app.py (Phần khai báo và hàm xử lý)

Mở file app.py trên GitHub và bấm biểu tượng cây bút để sửa đổi.

Ở phần đầu tiên của file (chỗ có các lệnh import), thầy thêm dòng này vào:

Python
import pandas as pd
import io
Ngay bên dưới phần khai báo thư viện, thầy dán hàm xử lý Excel này vào (hàm này có chức năng đọc các sheet, bỏ dòng trống và tự động điền các ô bị gộp - merged cells):

Python
def process_matrix_excel(uploaded_file):
    try:
        excel_file = pd.ExcelFile(uploaded_file)
        matrix_text = "CẤU TRÚC MA TRẬN VÀ BẢN ĐẶC TẢ CHI TIẾT:\n\n"
        
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
            # Xóa các dòng/cột rỗng hoàn toàn
            df = df.dropna(how='all').dropna(axis=1, how='all')
            # Điền dữ liệu cho các ô gộp (merged cells) thường gặp ở cột Chủ đề
            df = df.ffill(axis=0) 
            
            matrix_text += f"--- Phần: {sheet_name} ---\n"
            matrix_text += df.to_markdown(index=False) + "\n\n"
            
        return matrix_text
    except Exception as e:
        return f"Lỗi khi xử lý file Excel: {str(e)}"
Bước 3: Cập nhật giao diện tải file và tích hợp vào Prompt của Gemini

Cuộn chuột xuống phần thiết kế giao diện (nơi có các nút st.file_uploader), dán đoạn code sau để tạo thêm một ô tải file Excel:

Python
st.subheader("Cấu hình Ma trận")
matrix_file = st.file_uploader("Tải lên file Ma trận & Đặc tả (Excel .xlsx)", type=["xlsx"])
matrix_context = ""

if matrix_file is not None:
    matrix_context = process_matrix_excel(matrix_file)
    st.success("Đã trích xuất thành công dữ liệu từ file Excel!")
Tìm đến đoạn code cấu hình Prompt gửi cho Gemini (thường là biến prompt hoặc system_instruction). Thầy chèn biến matrix_context vào để AI đọc được quy luật. Ví dụ:

Python
full_prompt = f"""
Bạn là chuyên gia phân tích đề thi Toán THPT. Hãy dựa vào cấu trúc ma trận sau đây để phân loại và gán mã năng lực (TD/GQ/MH) cho từng câu hỏi:

{matrix_context}

NỘI DUNG ĐỀ THI CẦN PHÂN TÍCH:
{exam_content}
"""
# Gửi full_prompt này cho model Gemini xử lý
Bước 4: Lưu thay đổi và kiểm tra

Bấm nút màu xanh lá Commit changes... để lưu lại toàn bộ mã nguồn app.py vừa sửa.

Mở trình duyệt truy cập vào đường link Streamlit của hệ thống QTOAN Tools.

Không cần phải thao tác gì thêm trên Streamlit, hệ thống sẽ tự động tải lại (reboot) máy chủ trong khoảng 30 giây đến 1 phút và cập nhật giao diện mới có ô tải file Excel.

Thầy có thể tải trực tiếp file Ma_Tran_Dac_Ta_Toan_12.xlsx lên ô mới này, sau đó tải file Word đề thi vào ô cũ. Hệ thống sẽ tự động ghép nối cấu trúc ma trận chuẩn với đề thi thực tế để kết xuất ra 5 hạng mục định dạng chuẩn.

Create Google Docs
Create Word Docs
Create PDF Docs
Create Markdown File
import pandas as pd

import io

import streamlit as st

import google.generativeai as genai

import docx

from io import BytesIO



st.set_page_config(page_title="Hệ thống Ma trận & Đề thi - QTOAN Tools", layout="wide")

st.title("Hệ thống Tự động Phân tích Đề & Lập Ma Trận Toán Học")



with st.sidebar:

    st.header("Cấu hình hệ thống")

    

    # ⚠️ Đã sửa: Lấy API Key an toàn từ Streamlit Secrets để tránh lỗi 403 Leaked Key

    try:

        api_key ="AIzaSyCdZiVOLXn9s0S30PkCE_CYS45PLV28F6s"

    except KeyError:

        api_key = ""

        st.error("Chưa cấu hình GEMINI_API_KEY trong mục Secrets của Streamlit Cloud.")



    khoi_lop = st.radio("Chọn khối lớp:", ["Khối 6, 7, 8, 9, 10, 11", "Khối 12"])

    st.markdown("---")

    st.info("Định dạng bắt buộc:\n- Công thức: `$ ... $`\n- Hình vẽ: `TikZ`")

    st.markdown("**Bản quyền:** thầy Quang Toàn-dạy toán-0387997970")



uploaded_file = st.file_uploader("Đưa đề thi gốc vào đây (định dạng .txt hoặc Word)", type=["txt", "docx"])



if st.button("Khởi tạo Trọn Bộ (5 Hạng Mục)") and uploaded_file and api_key:

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

    

    # ⚠️ Đã sửa: Thêm hậu tố -latest để tránh lỗi 404 API Not Found

    model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest', system_instruction=system_instruction)

    

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

Dưới đây là mã nguồn app.py đã được rà soát và tối ưu hóa toàn diện. Các lỗi nghiêm trọng về bảo mật khóa API, lỗi bỏ sót bảng biểu trong file Word và luồng xử lý file ma trận Excel đã được tích hợp hoàn chỉnh.

Python
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
    
    # Bảo mật API Key qua st.secrets, chặn rò rỉ mã nguồn trên GitHub
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = st.text_input("Nhập API Key:", type="password")
        if not api_key:
            st.error("Chưa cấu hình GEMINI_API_KEY.")

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
    - Mọi công thức toán học phải bọc trong $ ... $. Tuyệt đối không dùng \\( ... \\).
    - Mọi hình vẽ, đồ thị, bảng biến thiên BẮT BUỘC vẽ bằng mã TikZ trong môi trường \\begin{{tikzpicture}} ... \\end{{tikzpicture}}.
    """
    
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
Loại bỏ mã API nhúng cứng (Hardcoded Key): Mã key bắt đầu bằng AIzaSy... đã bị xóa để tránh rủi ro bảo mật (lỗi 403) khi đẩy lên kho lưu trữ đám mây. Mã nguồn giờ đây gọi trực tiếp từ st.secrets["GEMINI_API_KEY"].

Trích xuất toàn vẹn bảng biểu Word: Hàm read_word_file mới không chỉ đọc văn bản thuần (paragraphs) mà quét qua toàn bộ cấu trúc lưới (doc.tables) để giữ lại hệ thống bảng đáp án hoặc bảng biến thiên có sẵn trong file Word đề gốc.

Tích hợp hàm đọc Excel: Giao diện tải file Ma_Tran_Dac_Ta_Toan_12.xlsx được bố trí gọn gàng tại thanh công cụ (sidebar). Cấu trúc của lưới ma trận tự động chuyển hóa thành chuỗi văn bản và chèn thẳng vào bộ nguyên tắc xử lý của mô hình.

Hiệu ứng xuất văn bản động (Streaming): Dữ liệu trả về từ Gemini được hiển thị theo thời gian thực (stream) thay vì đóng băng màn hình chờ xử lý toàn bộ, giúp quá trình phân tách mã năng lực trực quan hơn.

Create Google Docs
Create Word Docs
Create PDF Docs
Create Markdown File
cập nhật thêm các code

Tôi đã cập nhật và tạo sẵn 2 file mã nguồn cho hệ thống QTOAN Tools của thầy. Thầy chỉ cần tải về, mở file bằng Notepad (hoặc copy trực tiếp nội dung bên trong) và dán đè lên GitHub là xong:

File ứng dụng chính (đã tích hợp thuật toán đọc ma trận Excel, bảo mật API và hiển thị Stream):

Biểu tượng PY
app
 PY 
File khai báo thư viện (đã bổ sung pandas, openpyxl và tabulate để xuất bảng):

Biểu tượng TXT
requirements
 TXT 
Thầy lưu ý sau khi Commit changes 2 file này lên GitHub, hãy chờ khoảng 1 phút để nền tảng Streamlit Cloud tự động đồng bộ và khởi động lại trang web với giao diện mới nhé.

Thầy cần tôi hỗ trợ thiết lập phần bảo mật GEMINI_API_KEY trong mục Secrets của Streamlit luôn không?

Create Google Docs
Create Word Docs
Create PDF Docs
Create Markdown File
có

Để bảo mật tuyệt đối khóa API và tránh rủi ro rò rỉ mã trên GitHub, thầy thao tác thiết lập Streamlit Secrets theo các bước sau:

Truy cập trang quản lý ứng dụng:

Mở trình duyệt và vào lại đường link: share.streamlit.io.

Tại màn hình chính, thầy sẽ thấy danh sách các ứng dụng đã triển khai (ví dụ: qtoan-matrix-system).

Mở bảng Cài đặt (Settings):

Bấm vào biểu tượng dấu 3 chấm dọc (⋮) nằm ở bên phải tên ứng dụng của thầy.

Chọn mục Settings (Cài đặt) có hình bánh răng cưa.

Khai báo khóa bảo mật (Secrets):

Trong bảng Settings vừa hiện ra, nhìn sang menu bên trái, thầy chọn mục Secrets.

Tại khung soạn thảo lớn, thầy gõ (hoặc copy/paste) chính xác dòng lệnh sau:

Ini, TOML
GEMINI_API_KEY = "dán_chuỗi_api_key_rất_dài_của_thầy_vào_đây"
Lưu ý: Từ GEMINI_API_KEY phải viết hoa toàn bộ, và chuỗi mã khóa phải được đặt gọn bên trong cặp dấu ngoặc kép "".

Lưu thay đổi:

Bấm nút Save ở góc dưới cùng bên phải để hệ thống ghi nhận.

Ngay sau khi bấm Save, máy chủ Streamlit sẽ tự động khởi động lại trong vài giây. Từ thời điểm này, file app.py mới mà tôi vừa tối ưu sẽ tự động "hút" mã API từ khu vực an toàn này ra để sử dụng thông qua lệnh st.secrets["GEMINI_API_KEY"]. Mã nguồn trên GitHub của thầy hiện tại đã hoàn toàn "sạch", không ai có thể xem trộm được "chìa khóa" trí tuệ nhân tạo của QTOAN Tools nữa.

Create Google Docs
Create Word Docs
Create PDF Docs
Create Markdown File
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

    

    # Bảo mật API Key qua st.secrets, chặn rò rỉ mã nguồn trên GitHub

    try:

        api_key = st.secrets["GEMINI_API_KEY"]

    except Exception:

        api_key = st.text_input("Nhập API Key:", type="password")

        if not api_key:

            st.error("Chưa cấu hình GEMINI_API_KEY.")



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

Thầy có muốn tôi tải file app.py mới này lên kho chứa Google Drive hoặc đẩy trực tiếp lên GitHub không?

Create Google Docs
Create Word Docs
Create PDF Docs
Create Markdown File
AIzaSyCjGcynucVLaoxQeTyBj1ZEKFYAKUCSrvM

Thầy Toàn ơi, thầy vừa dán trực tiếp một mã API Key (bắt đầu bằng AIzaSy...) vào khung chat.

⚠️ Lưu ý bảo mật quan trọng:
Tuyệt đối không gửi khóa API vào các khung chat hoặc dán trực tiếp vào mã nguồn app.py đưa lên GitHub để tránh bị hệ thống quét và vô hiệu hóa khóa (tránh lặp lại lỗi rò rỉ khóa 403).

Để ứng dụng QTOAN Tools hoạt động an toàn, thầy hãy dùng chính khóa này để cấu hình trên Streamlit theo các bước sau:

Truy cập share.streamlit.io và mở bảng Settings (Cài đặt) của ứng dụng.

Tìm đến mục Secrets ở menu bên trái.

Soạn chính xác cú pháp sau (nhớ giữ nguyên cặp dấu ngoặc kép) và dán khóa của thầy vào:

Ini, TOML
GEMINI_API_KEY = "dán_khóa_thầy_vừa_gửi_vào_đây"
Bấm Save.

(Lưu ý thêm: Nếu khóa mã ...CSrvM này đã từng bị thầy dán nhầm vào file app.py và đẩy lên GitHub ở các lần thử trước, thầy nên vào lại Google AI Studio xóa nó đi và tạo hẳn một khóa mới tinh để cấu hình vào Streamlit nhé).

Thầy cấu hình xong bên Streamlit thì báo tôi biết để chúng ta kiểm tra thử tiến trình chạy của web nhé!

Create Google Docs
Create Word Docs
Create PDF Docs
Create Markdown File
Lỗi "403 Your API key was reported as leaked" xuất hiện trên màn hình chính là hệ quả của việc khóa API trước đó đã bị dán trực tiếp vào file mã nguồn và đẩy lên kho lưu trữ GitHub công khai. Hệ thống bảo mật của Google tự động quét kho dữ liệu, phát hiện rò rỉ và lập tức vô hiệu hóa vĩnh viễn khóa này để ngăn chặn người lạ dùng lén tài nguyên của thầy.   
image_458a8b.png

Để khắc phục triệt để và giúp hệ thống QTOAN Tools chạy trở lại, thầy thực hiện 3 bước sau:

Xóa khóa cũ và tạo khóa mới: Truy cập lại Google AI Studio, tìm các khóa cũ đã bị lộ (bao gồm cả mã khóa thầy gửi ở tin nhắn trước) và bấm biểu tượng thùng rác để xóa bỏ. Sau đó, bấm Create API key để sinh ra một khóa hoàn toàn mới.

Khai báo vào vùng an toàn của Streamlit: Mở trang quản lý share.streamlit.io, bấm vào dấu 3 chấm dọc bên cạnh tên ứng dụng -> chọn Settings -> chọn menu Secrets.

Cập nhật khóa: Xóa mã cũ đi và dán mã mới tinh vừa tạo vào theo đúng cú pháp (bắt buộc phải có cặp dấu ngoặc kép):

Ini, TOML
GEMINI_API_KEY = "dán_khóa_mới_tinh_vào_đây"
Sau khi bấm Save, Streamlit sẽ tự khởi động lại máy chủ trong vài giây. Thầy quay lại tab màn hình đang báo lỗi, không cần tải file lại từ đầu mà chỉ cần bấm lại nút Khởi tạo Trọn Bộ (5 Hạng Mục) là AI sẽ bắt đầu đọc đề thi và vẽ hình TikZ bình thường.   
image_458a8b.png

Bây giờ khóa mới đã được giấu an toàn trên máy chủ của Streamlit, mã nguồn trên GitHub có ai xem cũng không thể đánh cắp được nữa. Thầy làm thử và báo lại kết quả nhé!

Create Google Docs
Create Word Docs
Create PDF Docs
Create Markdown File
tao giao diện nhập keys

Mã nguồn app.py đã được cập nhật để loại bỏ phần st.secrets và thay thế bằng một ô nhập liệu (text input) trực tiếp trên giao diện thanh công cụ bên trái.

Đây là file mã nguồn mới nhất:

Biểu tượng PY
app
 PY 
Thầy tải file này về, chép đè lên file app.py trên GitHub. Khi đó, giao diện web sẽ hiện ra một ô "Nhập Google Gemini API Key" ở dạng mật khẩu (các ký tự bị ẩn thành dấu chấm để bảo mật).

Phương pháp này giúp giải quyết triệt để lỗi 403. Giờ đây, mã nguồn trên GitHub hoàn toàn không chứa bất kỳ khóa nào. Khi thầy chia sẻ link Streamlit cho các thầy cô khác trong tổ Toán, mỗi người sẽ tự dán khóa API của riêng họ vào ô này để sử dụng, đảm bảo an toàn tuyệt đối và không sợ bị khóa chéo.

Create Google Docs
Create Word Docs
Create PDF Docs
Create Markdown File






Gemini là một AI và có thể mắc sai sót.

Addressing a Streamlit API key error
Create Google Docs
Create Word Docs
Create PDF Docs
Create Markdown File
Settings
Claude Icon
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
app.py
Đang hiển thị app.py.
