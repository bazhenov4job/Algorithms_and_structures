def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)


print(gcd(12, 2048000000))
