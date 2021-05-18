a = float(input("Введите 3-х значное число: "))
x = a // 100
y = a // 10 % 10
z = a % 10
sum = x + y + z
proiz = x * y * z
print(f'{sum = }, {proiz = }')
