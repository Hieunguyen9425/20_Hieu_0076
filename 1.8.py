Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1 = input("Nhập chuỗi s1: ")
Nhập chuỗi s1: hello
>>> s2 = input("Nhập chuỗi s2: ")
... 
Nhập chuỗi s2: Python
>>> s3 = input("Nhập chuỗi s3: ")
... 
Nhập chuỗi s3: programing laguage
>>> index = int(input("Nhập chỉ mục index: "))
... 
Nhập chỉ mục index: 2
>>> print(f"Chiều dài của chuỗi s1: {len(s1)}")
Chiều dài của chuỗi s1: 5
>>> print(f"Chiều dài của chuỗi s2: {len(s2)}")
... 
Chiều dài của chuỗi s2: 6
>>> print(f"Chiều dài của chuỗi s3: {len(s3)}")
... 
Chiều dài của chuỗi s3: 18
>>> print(f"Lặp lại chuỗi s2 2 lần với nội dung 'Python': {s2_repeated}")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(f"Lặp lại chuỗi s2 2 lần với nội dung 'Python': {s2_repeated}")
NameError: name 's2_repeated' is not defined
>>> s2_repeated = s2 + "Python" + s2
... 
>>> print(f"Lặp lại chuỗi s2 2 lần với nội dung 'Python': {s2_repeated}")
Lặp lại chuỗi s2 2 lần với nội dung 'Python': PythonPythonPython
>>> s4 = s1[index:]
>>> KeyboardInterrupt
>>> print(f"Chuỗi s4 từ index {index} đến hết: {s4}")
Chuỗi s4 từ index 2 đến hết: llo
