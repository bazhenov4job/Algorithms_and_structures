"""Сортировка выбором"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def selection_sort(array):

    for i in range(len(array)):
        index_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[index_min]:
                index_min = j

        array[index_min], array[i] = array[i], array[index_min]
        print(array)


selection_sort(array)
print(array)
