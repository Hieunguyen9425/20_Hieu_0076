Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #!/bin/bash
... 
... # Hàm kiểm tra số hoàn hảo
... is_perfect_number() {
...     num=$1
...     sum_of_divisors=1
... 
...     for ((i=2; i<=num/2; i++)); do
...         if [ $((num % i)) -eq 0 ]; then
...             sum_of_divisors=$((sum_of_divisors + i))
...         fi
...     done
... 
...     if [ $sum_of_divisors -eq $num ]; then
...         echo "$num là số hoàn hảo."
...     else
...         echo "$num không phải là số hoàn hảo."
...     fi
... }
... 
... # Nhập số nguyên từ người dùng
... read -p "Nhập một số nguyên: " x
... 
... # Gọi hàm kiểm tra số hoàn hảo
... is_perfect_number $x
