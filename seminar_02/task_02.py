#for task 01
a = 73.0
print(f'{type(a)=}')

import sys

# task_02_вывести данные о каждом элементе, пронумеровать, хэк,значение, адес памяти и т.п.
data = [42, 73.0, 'Hello world!', True, 42, 'Hello!', 256, 2 ** 8, 1, 'привет, Мир!']

for nn, value in enumerate(data, 1):
    chech_int = 'Похоже на целое число' if isinstance(value, int) else ''
    chech_str = 'похоже на строку'if isinstance(value, str) else ''
    print(f'{nn}.Объект "{value}".\nАдрес в памяти {id(value)} \nРазмер в памяти {sys.getsizeof(value)}.\n'
          f'Хэш объекта {hash(value)}. \n{chech_int}{chech_str}\n')
