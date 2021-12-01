"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min = 0
max = 0
for i in range(len(array)):
    if array[min] >= array[i]:
        min = i
    if array[max] <= array[i]:
        max = i
array[min], array[max] = array[max], array[min]
        
print(array)
