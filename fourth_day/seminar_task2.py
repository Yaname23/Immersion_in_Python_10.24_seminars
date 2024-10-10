"""Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""

def uni(x):
    res = []
    for i in set(x):
        res.append(ord(i))
    res.sort(reverse=True)
    return res
_str = input('ВВедите строку:  ')
print(uni(_str))

print('-------2 вариант-----------')

str_ = 'Сформируйте список с уникальными кодами Unicode каждого'
print([ord(i) for i in sorted(list(set(str_)))[::-1]])