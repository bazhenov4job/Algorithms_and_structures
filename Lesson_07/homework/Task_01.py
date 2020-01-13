"""1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
сортировки, например, расчёской, шейкерная и другие в зачёт не идут."""
# В ходе улучшения алгоритма была достигнута сложность ниже чем О(n**2), считаю, что алгоритм улучшил

import random
array = [random.randint(-100, 100) for _ in range(100)]


def adv_bubble(array):
    j = 0
    # Эти две переменные добавлены для оптимизации алгоритма
    count = 0
    new_count = 0

    while j < len(array):

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                # Увеличиваем счётчик, показывающий наличие перестановки
                new_count += 1
        # Если в ходе сортировки перестановок не произошло, то массив считается отсортированным
        if count == new_count:
            print(f"Сортировка завершена, потребовалось произвести {count} перестановок.")
            break
        else:
            count = new_count
        j += 1
    return array


print(adv_bubble(array))