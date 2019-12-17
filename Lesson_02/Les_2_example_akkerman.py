import sys

sys.setrecursionlimit(3000)


def akker(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akker(m-1, 1)
    elif m > 0 and n > 0:
        return akker(m-1, akker(m, n-1))

print(akker(3,8))
