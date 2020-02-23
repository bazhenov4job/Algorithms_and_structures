a = [1, 3, 2]
b = ['first', 'third', 'second']

c = list(zip(a, b))
print(c)
c = sorted(c, key=lambda x: x[0])
print(c)
a = [x[0] for x in c]
b = [x[1] for x in c]
print(a, b, sep='\n')
