import random
from collections import deque

# Задача 1
array = [random.randint(-100, 100) for _ in range(100)]
print(array)

# array_below = []
# array_above = []
deq = deque()

for item in array:
    if item >= 0:
        deq.append(item)
    else:
        deq.appendleft(item)

print(deq)
# print(array_below)
