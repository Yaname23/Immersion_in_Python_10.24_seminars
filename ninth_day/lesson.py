print('____Замыкание______')


def func(a):
    x = 1
    res = x + a
    return res

x = 100 # Значение x из глобальной области видимости не принимается
print(func(5))


print('________Пример замыкания _________')
from  typing import Callable

def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    return add_two_str

print(add_one_str('Hello')('World'))

print('______еще__Пример замыкания _________')
from  typing import Callable

def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    return add_two_str

hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('World!'))
print(hello('friend!'))
print(bye('wonderful world!'))

print(f'{type(add_one_str) = }, {add_one_str.__name__ =}, {id(add_one_str) = }')
print(f'{type(hello) = }, {hello.__name__ =}, {id(hello) = }')
print(f'{type(bye) = }, {bye.__name__ =}, {id(bye) = }')

print('______замыкание измняеиые и неизменяемые объекты _________')

from  typing import Callable

def add_one(a: str) -> Callable[[str], str]:
    names = []
    def add_two(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)
    return add_two

hello = add_one('Hello')
bye = add_one('Good bye')

print(hello('Alex!'))
print(hello('Karina!'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))

print('----неизменяемые-----')

def add_one_str(a: str) -> Callable[[str], str]:
    text = ''
    def add_two_str(b: str) -> str:
        nonlocal text
        text += ', ' + b
        return a + text

    return add_two_str

hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Alex!'))
print(hello('Karina!'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))

print('---------функция в качестве аргумента-------------')

import time
def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}:  {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result

    return wrapper

def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

print(f'{factorial(1000) = }')
control = main(factorial)
print(f'{control.__name__= }')
print(f'{control(1000) = }')

print('---------дополнительная переменная в декораторе------------')

def cache(func: Callable):
    _cache_dict = {}

    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]

    return wrapper

@cache
def factorial(n: int) -> int:
    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

print(f'{factorial(10) = }')
print(f'{factorial(15) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')

print('----  -----')
