"""3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы."""
"""Применяем алгоритм вялой сортировки"""

data = [4, 2, 3, 1, 5]


def slow_rec(data, i, j):
    if i >= j:
        return data
    m = (i + j) // 2
    slow_rec(data, i, m)
    slow_rec(data, m + 1, j)
    if data[m] > data[j]:
        data[m], data[j] = data[j], data[m]
    slow_rec(data, i, j - 1)


def slow_sort(data):
    return slow_rec(data, 0, len(data) - 1)


def mediana(data):
    index = len(data) // 2
    med = data[index]
    return med, index


slow_sort(data)
print(data)
med, index = mediana(data)
print(f'В предложенном массиве медианой является {med}, с индексом {index}')
