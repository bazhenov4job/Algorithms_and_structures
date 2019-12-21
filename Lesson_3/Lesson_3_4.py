import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
for row in matrix:
    for item in row:
        print(f'{item:>4}', end='')
    print()

# Посчитать сумму столбцо и строк матрицы

sum_column = [0] * len(matrix)

for row in matrix:
    sum_line = 0

    for i, item in enumerate(row):
        sum_line += item
        sum_column[i] += item

        print(f'{item:>5}', end='')

    print(f'    |{sum_line}')
print('-' * (len(matrix) * 5))

for s in sum_column:
    print(f'{s:>5}', end='')
