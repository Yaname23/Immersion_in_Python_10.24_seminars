"""Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
from pathlib import Path
import json

def create_json_from_file(file_path):
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File '{file_path}' not found.")

    names = []
    numbers = []
    with file_path.open('r', encoding='utf-8') as f:
        for line in f:
            name, number = line.strip().split(' | ')
            names.append(name.upper())
            numbers.append(number)

    data = dict(zip(names, numbers))
    with open(file_path.parent / 'task01.json', 'w', encoding='utf-8') as f_json:
        json.dump(data, f_json, indent=4)
create_json_from_file('task_01.txt')

# def create_json_from_file():
#     with open('task_01.txt', 'r+', encoding='utf-8') as f:
#         print(list(f))
#     with open('task01.json', 'w', encoding='utf-8') as f_json:
#         names = []
#         numbers = []
#         for line in f:
#             name, number = line.strip().split(' | ')
#             names.append(name.upper())
#             numbers.append(number)
#         data = dict(zip(names, numbers))
#         json.dump(data, f_json, indent=4)
#
# create_json_from_file()

# --------------------------

