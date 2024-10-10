"""
Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.

"""
import random as rnd
from typing import Callable

def decor(func: Callable):

    def wrapper(*args, **kwargs):
        a, b, *_ = args
        if a not in range(1, 101):
            print('Загаданное число должно быть в диапазоне от 1 до 100 ')
            a = rnd.randint(1, 100)
        if b not in range(1, 11):
            print('Загаданное число должно быть в диапазоне от 1 до 10 ')
            b = rnd.randint(1, 10)
        func(a, b)

    return  wrapper
@decor
def inner(a: int, b: int):
    while b:
        guess = int(input(f'Угадайте число от {1} до {100} за {b} попыток: \n'))

        if guess > a:
            print(f'Загаданное число меньше чем {guess}')
        elif guess < a:
            print(f'Загаданное число больше чем {guess}')
        else:
            print(f'ты угадал, было загадано {a}')
            break
        b -= 1
    else:
        print(f'Ты не угадал за указанное число попыток число {a}')



inner(202, 5)