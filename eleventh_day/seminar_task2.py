"""Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра

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