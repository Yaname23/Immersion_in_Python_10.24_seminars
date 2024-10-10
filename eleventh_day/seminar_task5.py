"""Задание №5
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.

"""
import copy
class Archive:

    archive = []

    def __init__(self, value: int, text: str):
        self.value = value
        self.text = text
        self.archive = copy.deepcopy(self.__class__.archive)
        self.__class__.archive.append(tuple((value,text)))

    def __str__(self):
        return f'{self.value}{self.text} | {self.archive}'

a = Archive(1, 'text1')
b = Archive(2, 'text2')
c = Archive(3, 'text3')
print(a)
print(b)
print(c)