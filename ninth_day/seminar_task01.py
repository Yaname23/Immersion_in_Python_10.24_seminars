"""Задание №1
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""

import random as rnd

def outer():
    a = rnd.randint(1, 100)
    b = rnd.randint(1, 10)
    def inner():
        nonlocal a, b  # Обращение к локальным переменным из внешнего контекста

        while b:
            guess =int(input(f'Угадайте число от {1} до {100} за {b} попыток: \n'))
            if guess > a:
                print(f'Загаданное число меньше чем { guess}')
            elif guess < a:
                print(f'Загаданное число больше чем { guess}')
            else:
                print(f'ты угадал, было загадано {a}')
                break
            b -= 1
        else:
            print('Ты не угадал за указанное число попыток')


    return inner
primer = outer()
primer()
