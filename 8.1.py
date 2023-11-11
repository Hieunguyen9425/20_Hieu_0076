Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a, b, c, d = map(float, input("Nhập 4 số cách nhau bằng dấu phẩy: ").split(','))
... 
... 
Nhập 4 số cách nhau bằng dấu phẩy: 24,12,3,11
>>> so_lon_nhat = max(a, b, c, d)
>>> so_nho_nhat = min(a, b, c, d)
>>> print(f"Max = {so_lon_nhat}")
Max = 24.0
>>> print(f"Min = {so_nho_nhat}")
Min = 3.0
