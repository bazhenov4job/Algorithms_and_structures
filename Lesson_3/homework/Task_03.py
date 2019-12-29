"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random

# В этих словарях ключ - индекс элемента, значение - сам элемент. float('inf') - максимальное значение типа.

random_array = [random.randint(0, 100) for _ in range(30)]

print(random_array)

min_index = random_array[0]
max_index = random_array[0]

for i, value in enumerate(random_array):
    if value < min_index:
        min_index = value
    elif value > max_index:
        max_index = value

max_index = random_array.index(max_index)
min_index = random_array.index(min_index)

random_array[min_index], random_array[max_index] = random_array[max_index], random_array[min_index]

print(random_array)
