# Khởi tạo biến tổng
tong = 0

# Số lượng số nguyên cần tính tổng
n = int(input("Nhập số lượng số nguyên: "))

# Nhập các số nguyên và tính tổng
for i in range(n):
    so_nguyen = int(input(f"Nhập số nguyên thứ {i+1}: "))
    tong += so_nguyen

# In kết quả tổng
print(f"Tổng của các số nguyên là: {tong}")

