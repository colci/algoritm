SIZE = 10
MAX_ITEM = 99
result = [0 for _ in range(SIZE-2)]
for n in range(2, MAX_ITEM + 1):
    if n % 2 == 0:
        snum = 2
    else:
        snum = 3

    for i in range(snum, SIZE, 2):
        if n % i == 0:
            result[i-2] += 1

for i, res in enumerate(result):
    print(f'Чисел кратно {i+2} = {res}')
