import math

# Nhập giá trị của a, b, và c
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Kiểm tra giá trị của a
if a == 0:
    # Nếu a = 0, phương trình trở thành phương trình bậc nhất bx + c = 0
    if b != 0:
        x = -c / b
        print("Phương trình là bậc nhất và có nghiệm x =", x)
    else:
        if c != 0:
            print("Phương trình vô nghiệm.")
        else:
            print("Phương trình có vô số nghiệm.")
else:
    # Tính biệt thức Delta
    delta = b**2 - 4 * a * c

    if delta > 0:
        # Delta > 0, phương trình có hai nghiệm phân biệt
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        # Delta = 0, phương trình có nghiệm kép
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép: x =", x)
    else:
        # Delta < 0, phương trình vô nghiệm
        print("Phương trình vô nghiệm.")
