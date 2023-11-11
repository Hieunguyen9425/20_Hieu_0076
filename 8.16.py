# Hàm tính UCLN
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

# Nhập hai số nguyên từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tìm và in ra UCLN của a và b
ucln_ab = ucln(a, b)
print(f"Ước chung lớn nhất của {a} và {b} là: {ucln_ab}")
