print('________lambda_________')
def add_two_def(a,b):
    return a + b
add_two_lambda = lambda a, b: a + b

print(add_two_def(42, 3.14))
print(add_two_lambda(42, 3.14))

my_dict = {'two': 2, "one": 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1])
print(f'{s_key = }\n{s_value = }')
print('________map_и lambda________')
text = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda  x: x.lower(), text)
print(*res)
print('________filter_и lambda________')
numbers = [42, -73, 1024]
rec = tuple(filter(lambda x: x > 0, numbers))
print(rec)
print('________zip________')
names = ["Иван", "Николай", "Петр"]
salaries = [125_000, 96_000, 109_000]
awards =[0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards ):
    print(f'{name} заработал {salary: .2f} денег и премию {salary * award:.2f} ')

print('________max и min__и lambda_______')
lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000),("Николай", 96_000),("Пётр", 109_000)]
print(max(lst_1, default='empty'))
print(max(*lst_2))
print(max(lst_3, key=lambda  x: x[1]))
print('--min--')
print(min(lst_1, default='empty'))
print(min(*lst_2))
print(min(lst_3, key=lambda  x: x[1]))
print('________sum_________')
my_list = [42, 256, 73]
print(sum(my_list))
print(sum(my_list, start=1024))
print('________all_________')


def all_(iterable):
    for element in iterable:
        if not element:
            return  False
    return True


numbers = [42, -73, 1024]
if all(map(lambda  x: x > 0, numbers)):
    print("Все элементы положительные")
else:
    print("В последовательности есть отрицательные или нулевые элементы")


print('________any________')


def any_(iterable):
    for element in iterable:
        if not element:
            return  False
    return True


numbers = [42, -73, 1024]
if any(map(lambda  x: x > 0, numbers)):
    print("Хотябы один элемент положительный")
else:
    print("Все элементы не больше нуля")
print('________chr________')

print(chr(97))
print(chr(1105))
print(chr(128519))

print('________ord________')
print(ord('a'))
print(ord('а'))
print(ord('😉'))

print('________locals________')

SIZE = 10
def func(a, b, c):
    x = a + b
    print(locals())
    z = x + c
    return  z

func(1, 2, 3)

print('________globals________')

SIZE = 10
def funcs(a, b, c):
    x = a + b
    print(globals())
    z = x + c
    return  z

print(globals())
print(f'{funcs(1, 2, 3) = }')

x = 42
glob_dict = globals()
glob_dict['x'] = 73
print(f' {x = }')

print('________vars_______')
