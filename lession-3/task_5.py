import random
SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min = -1
for i in range(len(array)):
    if array[i] < 0 and min == -1:
        min = i
    elif array[i] < 0 and min != -1 and array[min] < array[i]:
        min = i
if min != -1:
    print(f'Максимальный отрицательный элемент = {array[min]}')
else:
    print("Нет отрицательных значений")
        
    
