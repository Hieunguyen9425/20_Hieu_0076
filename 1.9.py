Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lai_suat = float(input("Nhập lãi suất một năm (%): "))
Nhập lãi suất một năm (%): 7.6
>>> so_tien_gui = float(input("Nhập số tiền gửi (VNĐ): "))
... 
Nhập số tiền gửi (VNĐ): 10000000
>>> so_thang_gui = int(input("Nhập số tháng gửi: "))
... 
Nhập số tháng gửi: 6
>>> lai = (so_tien_gui * so_thang_gui) * (lai_suat / 100 / 12)
>>> tong_so_tien = so_tien_gui + lai
... 
>>> print(f"Tiền lãi = ({so_tien_gui} * {so_thang_gui}) * ({lai_suat} / 100 / 12) = {lai} VNĐ")
Tiền lãi = (10000000.0 * 6) * (7.6 / 100 / 12) = 380000.0 VNĐ
>>> print(f"Tiền vốn + lãi = {so_tien_gui} + {lai} = {tong_so_tien} VNĐ")
Tiền vốn + lãi = 10000000.0 + 380000.0 = 10380000.0 VNĐ
