class Person:
    max_up = 3

p1 = Person()
p2 = Person()

print(f'{Person.max_up = },{p1.max_up = }, {p2.max_up = }')

p1.max_up = 12
print(f'{Person.max_up = },{p1.max_up = }, {p2.max_up = }')

Person.max_up = 42
print(f'{Person.max_up = },{p1.max_up = }, {p2.max_up = }')

print('_________________')
Person.level = 1
print(f'{Person.level = },{p1.level = }, {p2.level = }')

p1.health = 100
print(f'{p1.health = }')
