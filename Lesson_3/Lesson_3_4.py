import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
for row in matrix:
    for item in row:
        print(f'{item:>4}', end='')
    print()
