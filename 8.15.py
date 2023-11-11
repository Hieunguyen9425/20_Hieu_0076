# Khởi tạo biến tổng
tong = 0

while True:
    so_nguyen = int(input("Nhập một số nguyên (Nhập 0 để kết thúc): "))
    
    if so_nguyen == 0:
        break  # Thoát khỏi vòng lặp nếu nhập số 0
    else:
        tong += so_nguyen

print(f"Tổng của các số nguyên là: {tong}")
