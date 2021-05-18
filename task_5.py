#Подразумеваем, что пользователь вводит только символы в нижнем регистре
a = input("Введите первую букву: ")
b = input("Введите вторую букву: ")

cod_a = ord(a)
cod_b = ord(b)
if (cod_a >= 97) and (cod_a <= 122) and (cod_b >= 97) and (cod_b <= 122):
    nom_a = cod_a - 96
    nom_b = cod_b - 96
    result = nom_b - nom_a - 1
    print(f'Буква {a} место в алфавите = {nom_a}')
    print(f'Буква {b} место в алфавите = {nom_b}')
    print(f'Между ними {result} букв.')
else:
    print("Ошибка ввода!")
