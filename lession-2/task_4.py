def get_sum_element(num, n):
    if n == 1:
        return num
    else:
        return num + get_sum_element(num / 2 * (-1), n - 1)

        
if __name__ == '__main__':
    n = int(input("Введите n количество элементов ряда: "))
    res = get_sum_element(1, n)
    print(f'Сумма ряда {res}')
