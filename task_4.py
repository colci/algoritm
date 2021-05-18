import random

print("Необходимо ввести диапазон для генерации целого числа")
start = int(input("Введите начало диапазона : "))
end = int(input("Введите окончание диапазона: "))
inum = random.randint(start, end)

print("Необходимо ввести диапазон для генерации случайного вешественного числа")
start = float(input("Введите начало диапазона: "))
end = float(input("Введите окончание диапазона: "))
fnum = random.uniform(start, end)

print("Введите диапазон символов алфавита для генерации случайного символа")
start = input("Введите символ начало диапазона: ")
end = input("Введите символ окончание диапазона: ")
simbol = chr(random.randint(ord(start), ord(end)))

print(f'Случайное целое число {inum}')
print(f'Случайное вешественное число {fnum}')
print(f'Случайное символ из диапазона {simbol}')
