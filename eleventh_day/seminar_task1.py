"""Задание №1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""
from datetime import datetime
class MyString(str):
    def __new__(cls, value: str, author: str ):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.creation_time = datetime.now()
        return instance


a = MyString('foo', 'bar')
print(a)
print(a.author)
print(a.creation_time)