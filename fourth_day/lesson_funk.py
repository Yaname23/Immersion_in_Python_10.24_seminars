print('______________________')
r = 42
print(type(r), id (r))
print(type(id))
print('________плохой стиль______________')
very_bad_programming_style = sum
print(very_bad_programming_style([1, 2, 3]))
print('______________________')
def quadratic_equations(a: int | float, b: int | float, c: int|float) -> tuple[float, float] | float | None:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2* a)
    elif d == 0:
        return  -b / (2 * a)
    else:
        return None
print(quadratic_equations(2, -3, -9))
print('__________изменяемые и неизменяемые аргументы____________')
print('__________неизменяемые аргументы____________')
def no_mutable(a: int) -> int:
    a += 1
    print(f'In func {a = }') # Для демонстрации работы, но не для привычки так делать
    return  a

a = 42
print(f'In main{a = }')
z = no_mutable(a)
print(f'{a = }\t{z =}')
print('__________изменяемые ____________')
def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = (item + 1)
    print(f'In finc {data = }')
    return data
my_list = [2, 4, 6, 8]
print(f'In main {my_list =}')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')
print('______________________')
def quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2* a)
    elif d == 0:
        return  -b / (2 * a)
    else:
        return None
print(quadratic_equation(2, -3, -9))
print('______________________')
def no_return(data: list[int]):
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'in func{data = }')

my_list = [2, 4, 6, 8]
print(f'In main {my_list =}')
new_list = no_return(my_list)
print(f'{my_list = }\t{new_list = }')
print('______________________')
def quadratic_equatio(a, b=0, c=0):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2* a)
    elif d == 0:
        return  -b / (2 * a)

print(quadratic_equatio(2, -9))
print('______________________')
def from_one_to_n(n, data=None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data

new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')
print('________позиционные и ключевые праметры_________')

def fnc(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parmeters):
    pass

def standart_arg(arg):
    print(arg)

standart_arg(42)
standart_arg(arg=42)
print('________пример только для ключевой функции_________')

def kwd_only_arg(*, arg):
    print(arg)

# kwd_only_arg(42)  так не работает
kwd_only_arg(arg=42)
print('________args и kwargs_________')
def mean(args):
    return  sum(args) / len(args)
print(mean([1, 2, 3]))
# print(mean(1, 2, 3))
print('___*args__')
def mean(*args):
    return  sum(args) / len(args)
print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))
print('___kwargs__')
def scool_print(**kwargs):
    for key, value in kwargs.items():
        print(f'по предмету "{key}" получена оценка {value}')
scool_print(химия=5, физика=4, математика=5, физра=5)
print('________локальная видимости_________')

def func(y: int) -> int:
    global x
    x += 100
    # x = 100
    print((f'in func {x = }'))
    return y + 1
x = 42
print(f'in main {x = }')
z = func(x)
print(f'{x = }\t{z = }')


print('________нелокальная видимости_________')
def main(a):
    x = 1
    def func(y):
        nonlocal x
        x += 100
        print((f'in func {x = }'))
        return y + 1

    return  x + func(a)

x = 42
print(f'in main {x = }')
z = main(x)
print(f'{x = }\t{z = }')
print('_________________')

LIMIT = 1_000

def func(x, y):
    result = x ** y % LIMIT
    return  result

print(func(42, 73))
