""" Быстрая сортировка Хоара без использования доп. памяти"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)
# Recursion depth indicator
level = 0


def quick_sort_no_memory(array, fst, lst, level=0):
    # fst - pointer where to start sort
    # lst - pointer where to stop sort

    if fst >= lst:
        return

    print(array)
    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <= j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quick_sort_no_memory(array, fst, j)
    quick_sort_no_memory(array, i, lst)

    # print('\t' * level, s_ar, m_ar, l_ar)
    # level += 1
    # return quick_sort(s_ar, level) + m_ar + quick_sort(l_ar, level)


quick_sort_no_memory(array, 0, len(array) - 1)
print(array)