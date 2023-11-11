def tinh_tien_thue_phong(ma_loai, so_dem):
    gia_phong = {
        1: 1260000,  # Standard
        2: 1550000,  # Superior Garden View
        3: 1830000,  # Superior Ocean View
        4: 1830000,  # Garden View Bungalow
        5: 2120000,  # Pool View Bungalow
        6: 2120000,  # Family Room
        7: 2540000,  # Beach Front Bungalow
        8: 4800000   # VIP Sea View
    }

    if ma_loai not in gia_phong:
        return "Mã loại phòng không hợp lệ."

    gia_1_dem = gia_phong[ma_loai]

    if so_dem == 1:
        return gia_1_dem
    elif so_dem >= 2 and so_dem <= 3:
        return gia_1_dem * so_dem * 0.75  # Giảm 25% cho 2-3 đêm
    elif so_dem >= 4:
        return gia_1_dem * so_dem * 0.7  # Giảm 30% cho từ 4 đêm trở lên

# Nhập mã loại phòng và số đêm muốn thuê
ma_loai = int(input("Nhập mã loại phòng (1-8): "))
so_dem = int(input("Nhập số đêm muốn thuê: "))

tien_thue_phong = tinh_tien_thue_phong(ma_loai, so_dem)
if isinstance(tien_thue_phong, str):
    print(tien_thue_phong)
else:
    print(f"Tổng tiền thuê phòng là: {tien_thue_phong} VND")
