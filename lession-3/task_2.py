import random
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

res = [i for i, num in enumerate(array) if num % 2 == 0]
print(res)
