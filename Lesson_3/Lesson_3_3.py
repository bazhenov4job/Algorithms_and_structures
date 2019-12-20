import random
# Задача 1
array = [random.randint(-100, 100) for _ in range(100)]
print(array)

array_below = []
array_above = []

for item in array:
    if item >= 0:
        array_above.append(item)
    else:
        array_below.append(item)

print(array_above)
print(array_below)

# Задача 2. Вставить в произвоьное место элемент. (Функция insert)

array = [random.randint(-100, 100) for _ in range(20)]
print(array)

num = int(input("Число для вставки: "))
pos = int(input(f"Позиция для вставки, не более{len(array)-1}: "))

array.append(None)
i = len(array) - 1

while i > pos:
    array[i], array[i-1] = array[i-1], array[i]
    i -= 1
array[pos] = num
print(array)
