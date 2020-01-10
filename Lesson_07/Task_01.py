"""Сортировка пузырьком"""

import random
import copy

size = 1000
array = [i for i in range(size)]
array_1 = copy.deepcopy(array)
random.shuffle(array)
print(array)

n = 1
k_new = 0
k_old = 0
while n < len(array):
    for i in range(len(array) - n):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            k_new += 1
    if k_new == k_old:
        break
    else:
        k_old = k_new
    n += 1

print(n)
print(array)
print(array == array_1)
