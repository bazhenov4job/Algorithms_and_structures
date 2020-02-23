"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""


from collections import Counter, OrderedDict
from binarytree import Node
from copy import deepcopy


def tree_search(tree, symbol, path=''):
    print(symbol, path, tree.value)
    if tree.value == symbol:
        print('нашёл', path)
        return path

    if tree.value == 0:
        path += '0'
        tree_search(tree.left, symbol, path)
        if tree.left != 0 and tree.left != symbol:
            path += '1'
            return tree_search(tree.right, symbol, path)


def haffman_encode(string):

    counted_chars = Counter(string)
    ordered_chars = OrderedDict(sorted(counted_chars.items(), key=lambda x: x[1]))

    while len(ordered_chars) > 1:
        left_value = ordered_chars.popitem(last=False)
        right_value = ordered_chars.popitem(last=False)
        char_tree = Node(0)
        if type(left_value[0]) == str:
            char_tree.left = Node(ord(left_value[0]))
        else:
            char_tree.left = left_value[0]

        if type(right_value[0]) == str:
            char_tree.right = Node(ord(right_value[0]))
        else:
            char_tree.right = right_value[0]

        ordered_chars[deepcopy(char_tree)] = left_value[1] + right_value[1]

    my_tree = ordered_chars.popitem()[0]
    print(my_tree)
    symbols = counted_chars.keys()
    # binary_dict = {}
    path = tree_search(my_tree, 98)
    print(path)

    return 0


print(haffman_encode('abrakadabra'))
