a = 5
b = 6
i = a & b
o = a | b
x = a ^ b
n = ~ a
right = a >> 2
left = a << 2

print(f'{a = } = {bin(a)}')
print(f'{b = } = {bin(b)}')
print(f'Битовое & {i} = {bin(i)}')
print(f'Битовое | {o} = {bin(o)}')
print(f'Битовое XOR {x} = {bin(x)}')
print(f'Битовое NOT {n} = {bin(n)}')
print(f'Результат сдвига в право над 5 на 2 бита {right} = {bin(right)}')
print(f'Результат сдвига в лево над 6 на 2 бита {left} = {bin(left)}')
