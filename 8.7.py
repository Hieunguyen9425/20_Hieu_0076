def tinh_tien_dien(kwh):
    if kwh <= 50:
        return kwh * 1678
    elif kwh <= 100:
        return 50 * 1678 + (kwh - 50) * 1734
    elif kwh <= 200:
        return 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
    elif kwh <= 300:
        return 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536
    elif kwh <= 400:
        return 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (kwh - 300) * 2834
    else:
        return 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (kwh - 400) * 2927

# Nhập số lượng kWh tiêu thụ
kwh = float(input("Nhập số kWh tiêu thụ: "))

tien_dien = tinh_tien_dien(kwh)
print(f"Số tiền điện cần thanh toán là: {tien_dien} VND")
