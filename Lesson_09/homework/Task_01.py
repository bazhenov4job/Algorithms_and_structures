"""
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется
вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
не решённой.
"""
from hashlib import sha1


def sub_string_count(string):

    count = 0
    hash_string = sha1(string.encode('utf-8')).hexdigest()
    for i in range(len(string) - 1):
        for j in range(i + 1, len(string)):
            subs = sha1(string[i: j].encode('utf-8')).hexdigest()


string = input('Введите строку')
print(f'число подстрок равно {sub_srting_count(string)}')
