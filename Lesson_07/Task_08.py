"""Сортировка сложных структур с использованем ключа"""

from collections import namedtuple
from operator import attrgetter

Person = namedtuple('Person', 'name, age')

p_1 = Person('Vasya', 25)
p_2 = Person('Kolya', 30)
p_3 = Person('Olya', 23)

people = [p_1, p_2, p_3]

print(people)

result = sorted(people)
print(result)

result_1 = sorted(people, key=lambda people: people.age)
print(result_1)

result_2 = sorted(people, key=attrgetter('age'))
print(result_2)