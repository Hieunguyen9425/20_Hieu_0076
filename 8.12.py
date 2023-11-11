Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Nhập số x
... x = int(input("Nhập số x: "))
... 
... # Kiểm tra x có phải là số nguyên tố
... is_prime = True
... 
... if x <= 1:
...     is_prime = False
... else:
...     for i in range(2, int(x**0.5) + 1):
...         if x % i == 0:
...             is_prime = False
...             break
... 
... # In kết quả
... if is_prime:
...     print(f"{x} là số nguyên tố.")
... else:
