a = int(input("Введите число"))
res = 0
even_number = 0
no_even_number = 0
while a > 0:
    res = a % 10
    if res % 2 == 0:
        even_number += 1
    else:
        no_even_number += 1
    a //= 10
print(f'В веденом числе четных = {even_number}, не четных = {no_even_number}')
