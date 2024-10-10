class NemedInt(int):
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'создал клaсс  {cls }')
        return instance

print('Создаём первый раз ')
a = NemedInt(42, 'главный ответ жизни, Вселенной и вообще')
print('Создаём второй раз ')
b = NemedInt(73, 'лучше простое число')

print(f'{a = }\t{a.name = }\t{type(a) = }')
print(f'{b = }\t{b.name = }\t{type(b) = }')
c = a + b
print(f'{c = }\t{type(c) = }')