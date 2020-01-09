import sys

print(sys.platform, sys.version)

a = 5
b = 125.54
c = 'Hello World!'

# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))

lst = [i for i in range(10)]
# print(sys.getsizeof(lst))
total_size = 0


memory_dic = {}
def show_size(x, level=0, size=0):
    print('\t' * level, f'type={x.__class__}, size = {sys.getsizeof(x)}, object={x}, reference={id(x)}')
    size = sys.getsizeof(x)
    if id(x) in memory_dic.keys():
        memory_dic[id(x)] += sys.getsizeof(x)
    else:
        memory_dic[id(x)] = sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                size += show_size(xx, level + 1, size)
        elif not isinstance(x, str):
            for xx in x:
                size += show_size(xx, level + 1, size)

    return size


size_a = show_size(a)

size_b = show_size(b)


size_c = show_size(lst)

# print('*' * 50)
#
t = tuple(lst)
size_t = show_size(t)

#
# print('*' * 50)
#
# r = set(lst)
# show_size(r)
#
# print('*' * 50)
#
d = {str(i): i for i in range(10)}

print(len(memory_dic), sum(memory_dic.values()))
