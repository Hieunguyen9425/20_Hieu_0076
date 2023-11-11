# Hàm tính BCNN
def bcnn(a, b):
    return (a * b) // ucln(a, b)

# Hàm tính UCLN
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

# Nhập hai số nguyên từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tính và in ra BCNN của a và b
bcnn_ab = bcnn(a, b)
print(f"Bội chung lớn nhất của {a} và {b} là: {bcnn_ab}")
