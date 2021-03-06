"""Прелставление чисел в разных системах счисления"""
a = 42
print(bin(a))
print(oct(a))
print(hex(a))

b = 0b100110
print(b)
# Аргумент base определяет в какой системе счисления задано число
c = int('2cd50', base=24)
print(c)

z = int('z', base=36)
print(z)

# Функция ord() позволяет получить код символа в кодировке ASCII
print(ord('d'))
# Символы кириллицы находятся в кодиовке UTF-8 и под них выделяется больше места в памяти
print(ord('л'))
