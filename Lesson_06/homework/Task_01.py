"""Определить, какое число в массиве встречается чаще всего."""
"""В ходе решения я модифициоровал функцию show_size, написанную преподавателем на уроке"""

import random
import sys

memory_dic = {}
# в массиве содежаться имена переменных, используемые для оценки памяти
exclusion_list = ['memory_dic', 'x', 'level', 'xx', 'size', 'exclusion_list']


def show_size(x, level=0, size=0):
    # Заполняем массив, определяя все используемые адреса и количество памяти, хранимое в них
    size = sys.getsizeof(x)
    memory_dic[id(x)] = sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                size += show_size(xx, level + 1, size)
        elif not isinstance(x, str):
            for xx in x:
                size += show_size(xx, level + 1, size)

    return size


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

# Берём список всех переменных исключая служебные и используемые в функции show_size
for var in dir():
    if not var.startswith('__'):
        if var not in exclusion_list:
            show_size(globals()[var])

print("Оценка памяти")
for key, value in memory_dic.items():
    print(f'По адресу {key} было размещено {value} бит памяти')
print()
print(f'Всего было использовано {len(memory_dic)} адресов, занято {sum(memory_dic.values())} бит памяти')





