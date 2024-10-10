print('------однострочник для перемены данных местами------')
a = 42
b = 73
a, b = b, a
print(f'{a = }\t{b = }')

print('------  распаковк и упаковка------')

# a, b, c = input('Введите 3 символа слитно: ')
# print(f'{a=} {b=} {c=}')

print("__________")
a, b, c = ('one', 'two', 'three')
print(f'{a=} {b=} {c=}')

print("__________")
data = ['один','два','три','четыре','пять','шесть','семь']
a, b, c, *d = data
print(f'{a=} {b=} {c=}{d=}')

a, b, *c, d = data
print(f'{a=} {b=} {c=}{d=}')

a, *b, c, d = data
print(f'{a=} {b=} {c=}{d=}')

*a, b, c, d = data
print(f'{a=} {b=} {c=}{d=}')

print("\n___с ссылкой_______")
link = ('https://gb.ru/lessons/443906')
prefix, *_, suffix = link.split('/')

print("\n___с for_______")
data =[2, 4, 6, 8, 10]
for item in data:
    print(item, end='\t')
print()
print("____или без for_____")
data =[2, 4, 6, 8, 10]
print(*data,sep='\t')

print("\n___множественное присваивание и сравнение_______")
a =b = c = 0 #хорошо
a += 42
print(f'{a=} {b=} {c=}')

a =b = c = {1, 2, 3}# очень плохо
a.add(42)
print(f'{a=} {b=} {c=}')

print("\n__________")
a, b, c = 1, 2, 3
print(f'{a=} {b=} {c=}')

t = 1, 2, 3
print(f'{t=}, {type(t)}')

print("\n____множественное сравнение______")
a = b = c = 42

if a == b == c:
    print('полное совпадение')
if a < b < c:
    print('b больше a и меньше c')

print("\n____с упорядочиванием______")
data = {10, 9, 8, 1, 6, 3}
a, b, c, *d, e = data
print(a, b, c, d, e)

print("\n____ИТЕРАТоРЫ______")
a = 42
data =[2, 4, 6, 8 ]
list_iter = iter(data)
print(list_iter)

data =[2, 4, 6, 8 ]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)

print("\n_____c подгрузкой днных из файла .bin _____")
data =[2, 4, 6, 8 ]
import  functools

f = open('mydata.bin', 'rb')
for block in iter(functools.partial(f.read,16), b''):
    print(block)
f.close()

print("\n_____next() _____")

# data =[2, 4, 6, 8 ]
# list_iter = iter(data)
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))

print("\n_____с тем что выше закоmментировано не работает _____")
data =[2, 4, 6, 8 ]
list_iter = iter(data)
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))

print("\n_____ГЕНЕРАТОРЫ _____")
a = range(0, 10, 2)
print(f'{a=}, {type(a)=},{a.__sizeof__()=},{len(a)}')
b = range(-1_000_000, 1_000_000, 2)
print(f'{b=}, {type(b)=},{b.__sizeof__()=},{len(b)}')

print("\n_____ распечатка алфавита циклом построчно_____")
my_gen =(chr(i) for i in range(97, 123))
print(my_gen)
for char in my_gen:
    print(char)
print("\n_____ _____")
x = [1, 1, 2, 3, 5, 8, 13]
y=[1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res)=}\n{res}')

print("\n_____распечатка алфавита циклом построчно и в одну строку _____")
my_listcom = [chr(i) for i in range(97, 123)]
print(my_listcom)
for char in my_listcom:
    print(char)

print("\n_____ _____")
data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)
print(f'{res= }')
data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res= }')

print("\n_____ _____")
x = [1, 1, 2, 3, 5, 8, 13]
y=[1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
print(f'{len(res)=}\n{res}')

mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
for item in mult:
    print(f'{item =}')

print("\n_____генератор множеств _____")
my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp)
for char in my_setcomp:
    print(char)

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)=}\n{res}')

print("\n_____генератор словарей _____")
my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp)
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')
