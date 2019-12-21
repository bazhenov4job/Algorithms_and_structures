# list_1 = [1, 2, 3, 4]
# list_2 = [1, 2, 3, 4]
# list_3 = [1, 2, 3, 4]
# list_4 = [1, 2, 3, 4]

# 1

# for i, item in enumerate(list_1):
#     del item
#
# print(list_1)
#
# for i, item in enumerate(list_2):
#     list_2.remove(item)
#
# print(list_2)
#
# for i, item in enumerate(list_3):
#     list_3.pop(i)
#
# print(list_3)
#
# for i, item in enumerate(list_4[:]):
#     list_4.remove(item)
#
# print(list_4)

# 2

# row = [''] * 3
# board = [row] * 3
# print(board)
# board[0][0] = 'X'
# print(board)
# board = [[''] * 3 for _ in range(3)]
# print(board)
# board[0][0] = 'X'
# print(board)

# 3
# a = [1, 2, 3]
# b = a
# a = a + [5, 6, 7]
# print(a, b)
#
# a = [1, 2, 3]
# b = a
# a += [5, 6, 7]
# print(a, b)

# 4
# t = ('one', 'two')
# for x in t:
#     print(x)
#
# t = ('one')
# for x in t:
#     print(x)
#
# t = ('one',)
# for x in t:
#     print(x)

# 5
# lst = [1, 2, 3, 3, 1, 4, 4, 15, 1, 14, 142, 414, 4]
# lst = (list(set(lst)))
# print(lst)

# 6

set_x = [1, 2, 3]
lst_x = [4, 5, 6]
dict_x = {frozenset(set_x): lst_x}
print(dict_x)
dict_x = {tuple(lst_x): lst_x}
print(dict_x)
