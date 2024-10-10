"""Задание №2
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку. """

txt = 'london is the capital of great britain'
dict_txt = {elem: ord(elem) for elem in txt}
me_gen_dict = ({elem: ord(elem)} for elem in txt)
print(dict_txt)
print(*me_gen_dict)

"""Задание №3
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""
iter_dict = iter(dict_txt.items())
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))


