a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a < b and a < c:
    if b > c:
        print(f'Средним число является третье число {c}')
    else:
        print(f'Средним число является второе число {b}')
elif a > b:
    if b > c:
        print(f'Средним число является третье число {с}')
    else:
        print(f'Средним число является первое число {a}')
else:
    print(f'Средним число является первое число {a}')