from collections import namedtuple


hero_1 = ('Ludvig', 'human', 100, 0.0, 250)


class Person:

    def __init__(self, name, race, health, mana, strength):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.strength = strength


hero_2 = Person('Ludvig', 'Human', 100, 0.0, 250)


New_person = namedtuple('New_person', 'name, race, health, mana, strength')
hero_3 = New_person('Ludvig', 'human', 100, 0.0, 250)
print(hero_3.name)

prop = ['name', '_race', '1health', 'mana', 'strength']
New_person_1 = namedtuple('New_person_1', prop, rename=True)
hero_4 = New_person_1('Ludvig', 'human', 100, 0.0, 250)
print(hero_4)

print('+' * 50)
Point = namedtuple('Point', 'x, y, z')

p1 = Point(2, z=3, y=4)
print(p1)

t = [5, 10, 15]
p2 = Point._make(t)
print(p2)

d2 = p2._asdict()
print(d2)

p3 = p2._replace(x=6)
print('=' * 50)
print(p2)
print(p3)

print(p3._fields)

New_point = namedtuple('New_point', 'x, y, z', defaults=[0, 0])
p4 = New_point(2)
print(p4)

print(p4._fields_defaults)

dict = {'x':2, 'y':3, 'z':4}
p5 = New_point(**dict)
print(p5)
print(p5.x)
