# Hàm kiểm tra số Armstrong
def is_armstrong_number(num):
    # Chuyển số thành chuỗi để đếm số chữ số
    digits = str(num)
    num_digits = len(digits)
    
    # Tính tổng các chữ số lũy thừa với số lượng chữ số
    total = sum(int(digit) ** num_digits for digit in digits)
    
    # Kiểm tra xem tổng có bằng số ban đầu không
    return total == num

# Nhập số từ người dùng
number = int(input("Nhập một số nguyên: "))

# Kiểm tra và in kết quả
if is_armstrong_number(number):
    print(f"{number} là số Armstrong.")
else:
    print(f"{number} không phải là số Armstrong.")
