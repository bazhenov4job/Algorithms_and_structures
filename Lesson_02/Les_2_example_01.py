def recursion(a, b):
    if a == b:
        return str(a)
    elif a > b:
        return str(a) + recursion(a-1, b)
    else:
        return str(a) + recursion(a+1, b)


print(recursion(1, 10000))
