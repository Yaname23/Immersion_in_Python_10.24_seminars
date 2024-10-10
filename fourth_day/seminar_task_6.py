"""Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""


def func(lst: list[int], lower: int, upper: int) -> int:
    lower, upper = sorted([lower, upper])
    # if upper > len(lst):
    #     upper = len(lst) - 1
    # if lower < 0:
    #     lower = 0
    return sum(lst[lower:upper+1])

print(func([1,2,3,4,5,6,7,8,9], 5, 2))

print('-------2 вариант-----------')

