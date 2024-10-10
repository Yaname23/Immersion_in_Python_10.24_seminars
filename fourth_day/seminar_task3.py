"""Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""

def dict_uni(x):
    lst = x.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])

    lst.sort()
    dct = {chr(i):i for i in range(lst[0], lst[1])}
    return dct

_str = input('Введите 2 числа: ')
print(dict_uni(_str))

print('-------2 вариант-----------')

def dict_uncode(some_str: str) -> dict:
    lims = [int(i) for i in some_str.split()]
    return {chr(i): i for i in range(min(lims), max(lims) + 1)}
print(dict_uncode('1123 1145'))