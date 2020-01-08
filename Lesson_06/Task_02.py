lst = []

lst.append(1)
lst.extend([2, 3, 4])

print(id(1), id(lst[0]))
lst.insert(1, 5)
print(lst)

last = lst.pop()
print(last, lst)
last = lst.pop()
print(last, lst)

lst.remove(5)
print(lst)
