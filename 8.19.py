# Nhập số n từ bàn phím
n = int(input("Nhập số n: "))

# Tạo danh sách các số lẻ từ 1 đến n
numbers = list(range(1, n + 1, 2))

# Đảo ngược danh sách
reversed_numbers = numbers[::-1]

# In ra kết quả
print("Dãy số sau khi đảo ngược và chỉ hiện số lẻ:")
for number in reversed_numbers:
    print(number, end=" ")
