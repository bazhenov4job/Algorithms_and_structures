"""3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
 от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита
 от 'a' до 'f' включительно."""

import random
import string

ans = input("Введите \'n\' для целых чисел, \'z\' для действительных, \'a\' для букв латиницы: ")

if ans.lower() == 'n':
    a_min = int(input("Введите наименьшее число диапазона: "))
    a_max = int(input("Введите наибольшее число диапазона: "))
    p = random.randint(a_min, a_max)
elif ans.lower() == 'z':
    a_min = float(input("Введите наименьшее число диапазона: "))
    a_max = float(input("Введите наибольшее число диапазона: "))
    p = random.uniform(a_min, a_max)
elif ans.lower() == 'a':
    alpha = string.ascii_lowercase
    a_min = (input("Введите начальную букву диапазона: "))
    a_max = (input("Введите полседнюю букву диапазона: "))
    ind_min = alpha.find(a_min)
    ind_max = alpha.find(a_max)
    ind_rand = random.randint(ind_min, ind_max)
    p = alpha[ind_rand]

print("Полученное случайное значение: {}".format(p))
