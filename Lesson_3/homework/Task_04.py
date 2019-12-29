"""Определить, какое число в массиве встречается чаще всего."""

import random

array = [random.randint(0, 10) for _ in range(50)]
number_count = {}
print(array)
for value in array[1:]:
    if value in number_count:
        number_count[value] += 1
    else:
        number_count[value] = 1
print(number_count)
max_count = {array[0]: number_count[array[0]]}

for key, value in number_count.items():
    for max_key, max_value in max_count.items():
        if number_count[key] > max_count[max_key]:
            max_count[key] = value
            max_count.pop(max_key)

print(max_count)
