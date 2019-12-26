"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных
значения."""

import random

array = [random.randint(-10, 10) for _ in range(50)]
max_negative = float('-inf')
for x in array:
    if x < 0:
        if x > max_negative:
            max_negative = x

print(max_negative)
