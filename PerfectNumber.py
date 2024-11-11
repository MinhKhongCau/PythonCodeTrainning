# Hàm kiểm tra số hoàn hảo
def is_perfect_number(num):
    if num < 1:
        return False  # Số hoàn hảo phải lớn hơn 0

    total = 0
    # Tìm các ước số từ 1 đến num/2
    for i in range(1, num // 2 + 1):
        if num % i == 0:  # Kiểm tra i có phải là ước của num không
            total += i  # Cộng các ước số

    # Kiểm tra tổng các ước số có bằng số ban đầu không
    return total == num

# Nhập số từ người dùng
number = int(input("Nhập một số nguyên dương: "))

# Kiểm tra và in kết quả
if is_perfect_number(number):
    print(f"{number} là số hoàn hảo.")
else:
    print(f"{number} không phải là số hoàn hảo.")
