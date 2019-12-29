"""Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3,
15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), т. к.
именно в этих позициях первого массива стоят четные числа."""

import random

first_array = [random.randint(0, 20) for _ in range(30)]
second_array = []

for i, value in enumerate(first_array):
    if value % 2 == 0:
        second_array.append(i)

# Вывод решения и проверка

for i in second_array:
    print(f'{i} - {first_array[i]}')
