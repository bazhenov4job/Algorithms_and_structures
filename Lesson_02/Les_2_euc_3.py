def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m


print(gcd(12, 2048000000))
