a = int(input("Введите"))
res = 0
while a > 0:
    res *= 10
    res += a % 10
    a //= 10
print(res)
