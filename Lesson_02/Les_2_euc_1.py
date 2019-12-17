def gcd(m, n):
    while (m != n):
        if m > n:
            m -= n
        else:
            n -= m
    return m


print(gcd(12, 2048000000))
