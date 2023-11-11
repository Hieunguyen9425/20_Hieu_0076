a = float(input("Nhập cạnh a:"))
b = float(input("Nhập cạnh b:"))
c = float(input("Nhập cạnh c:"))
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
print(f"Diện tích tam giác = {S}")