

a = '1,2,3,4,5,6'
b = a.split(',')
print(b)
b = list(map(int, b))
print(b, type(b[0]))
