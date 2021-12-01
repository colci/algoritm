"""В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""
import random
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
#первые два назначаем по умолчанию минимальными
min1 = 0
min2 = 1
for i in range(2, len(array)):
    if array[i] < array[min1]:
        if array[i] < array[min2] and array[min1] < array[min2]:
            min2 = i
        else:
            min1 = i
    elif array[i] < array[min2]:
        min2 = i
   
print(f'Первое наименьштй элемент масива {array[min1]} и второй {array[min2]}')
    
