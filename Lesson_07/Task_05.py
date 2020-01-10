""" Быстрая сортировка Хоара с использованием доп. памяти"""

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)
# Recursion depth indicator
level = 0


def quick_sort(array, level=0):

    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    # small array
    s_ar = []
    # medium array
    m_ar = []
    # large array
    l_ar = []

    for item in array:
        if item < pivot:
            s_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        else:
            raise Exception('Случилось непредвиденное')
    print('\t' * level, s_ar, m_ar, l_ar)
    level += 1
    return quick_sort(s_ar, level) + m_ar + quick_sort(l_ar, level)


array_new = quick_sort(array)
print(array_new)