import re

def is_valid_email(email):
    # Biểu thức chính quy để kiểm tra địa chỉ email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Kiểm tra chuỗi email có khớp với biểu thức chính quy không
    return re.match(email_pattern, email) is not None

# Nhập chuỗi từ người dùng
email_input = input("Nhập địa chỉ email: ")

# Kiểm tra và in kết quả
if is_valid_email(email_input):
    print(f"{email_input} là một địa chỉ email hợp lệ.")
else:
    print(f"{email_input} không phải là một địa chỉ email hợp lệ.")