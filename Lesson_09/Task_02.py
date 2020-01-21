"""Функция принимает на вход бинарное дерево поиска и число.
Будет идти по дереву искать число, а когда найдёт вернёт путь до него"""


from binarytree import bst


def search(bin_search_tree, number, path=''):

    if bin_search_tree.value == number:
        return f'Число {number} обнаружено по следующему пути: \nКорень {path}'



bt = bst(heght=5, is_perfect=False)
print(bt)
num = int(input('Введите число для поиска: '))
print(search(bt, num))
