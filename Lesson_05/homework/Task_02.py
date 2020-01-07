from collections import deque
from copy import deepcopy


hex_dec_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
dec_hex_dict = {value: key for key, value in hex_dec_dict.items()}


def add_hex(num_1, num_2):

    num_1 = deque(num_1)
    num_2 = deque(num_2)
    num_1.reverse()
    num_2.reverse()

    if len(num_1) >= len(num_2):
        pass
    else:
        num_1, num_2 = num_2, num_1

    result = deque()
    digit_transition = 0
    for i in range(len(num_1)):
        digit_num_1 = hex_dec_dict[num_1[i]]
        try:
            digit_num_2 = hex_dec_dict[num_2[i]]
        except IndexError:
            digit_num_2 = 0

        digit_sum = digit_num_1 + digit_num_2 + digit_transition
        if digit_sum >= 16:
            remainder = digit_sum % 16
            digit_transition = digit_sum // 16
            result.appendleft(dec_hex_dict[remainder])
            if i == len(num_1) - 1:
                result.appendleft('1')
        else:
            result.appendleft(dec_hex_dict[digit_sum])
            digit_transition = 0
    return list(result)


def mult_hex(num_1, num_2):
    result = deque()
    num_1 = deque(num_1)
    num_2 = deque(num_2)
    num_1.reverse()
    num_2.reverse()
    if len(num_1) < len(num_2):
        num_1, num_2 = num_2, num_1

    for i in range(len(num_2)):
        row_result = deque()
        floor = 0
        for j in range(len(num_1)):
            multiplication = hex_dec_dict[num_2[i]] * hex_dec_dict[num_1[j]] + floor

            if multiplication >= 16:
                remainder = multiplication % 16
                floor = multiplication // 16
                row_result.appendleft(dec_hex_dict[remainder])
                if j == len(num_1) - 1:
                    row_result.appendleft(dec_hex_dict[floor])
            else:
                row_result.appendleft(dec_hex_dict[multiplication])
                floor = 0
        for zeros in range(i):
            row_result.append('0')
        result = add_hex(result, row_result)

    return list(result)


hex_1 = list(input("Введите первое из шестнадцатеричных чисел: ").upper())
hex_2 = list(input("Введите второе из шестнадцатеричных чисел: ").upper())

print(f'{add_hex(hex_1, hex_2)} - результат сложения Ваших чисел')
print(f'{mult_hex(hex_1, hex_2)} - результат умножения Ваших чисел')
