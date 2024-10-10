"""Задание №5
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""

from seminar_task03 import decor as json_decor
from seminar_task2 import decor as param_control_decor
from seminar_task04 import outer as counter


@counter(2)
@json_decor

@param_control_decor



def guess_number(a: int, b: int):
    while b:
        guess = int(input(f'Угадайте число от {1} до {100} за {b} попыток: \n'))

        if guess > a:
            print(f'Загаданное число меньше чем {guess}')
        elif guess < a:
            print(f'Загаданное число больше чем {guess}')
        else:
            print(f'ты угадал, было загадано {a}')
            return True
        b -= 1
    else:
        print(f'Ты не угадал за указанное число попыток,загаданное число: {a}')
        return False

guess_number(321, 2)