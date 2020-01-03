from collections import ChainMap


d1 = {'a': 2, 'b': 4, 'c': 6}
d2 = {'a': 10, 'b': 20, 'd': 40}

d_map = ChainMap(d1, d2)
print(d_map)
d2['a'] = 100
print(d2)

print(d_map['a'])
print(d_map['d'])
print(d_map)

print('*' * 50)
x = d_map.new_child({'a': 111, 'b': 222, 'c': 333, 'd': 444})
print(x)

print(x.maps[0])
print(x.maps[-1])

print(x.parents)


print('*' * 50)
y = d_map.new_child()
print(y)
print(y['a'])
y['a'] = 1
print(y['a'])

print(list(y))
print(list(y.values()))
