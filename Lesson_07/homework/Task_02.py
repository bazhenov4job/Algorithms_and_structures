"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

"""Пытался сам сделать, но на 100% мне этого не удалось. Алгоритм сложный, двойная рекурсия.
Надеюсь, когда-нибудь мы все научимся так мыслить)))"""


from random import randint
array = [randint(-50, 50) for _ in range(8)]
# array = [4, 2, 3, 1, 6, 7, 8, 9]
print(array)


def merge_array(left_array, right_array):
    result_array = []
    len_left = len(left_array)
    len_right = len(right_array)
    left_index = right_index = 0

    for _ in range(len_left + len_right):
        if left_index < len_left and right_index < len_right:
            if left_array[left_index] <= right_array[right_index]:
                result_array.append(left_array[left_index])
                left_index += 1
            else:
                result_array.append(right_array[right_index])
                right_index += 1
        elif left_index == len_left:
            result_array.append(right_array[right_index])
            right_index += 1
        elif right_index == len_right:
            result_array.append(left_array[left_index])
            left_index += 1
    print(result_array)
    return result_array


def merge_sort(array, level=0):

    if len(array) == 1:
        return array
    else:
        left_array = merge_sort(array[:len(array) // 2])
        right_array = merge_sort(array[len(array) // 2:])

        # level += 1
        # print('\t' * level, left_array, right_array, level)

        return merge_array(left_array, right_array)


array = merge_sort(array)
print(array)
