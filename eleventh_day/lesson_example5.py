class User:

    def __init__(self, name: str):
        self.name = name
        print(f'Создан экземпляр с именем {self.name =}')

    def __del__(self):
        print(f'Удален экземпляр с именем {self.name}')

u_1 = User('Спенгер')
u_2 = User('Венкман')


print("______пример 2________")
import sys

class User2:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __del__(self):
        print(f'Удален экземпляр {self.name}')


u_1 = User2('Спенгер')
print(sys.getrefcount(u_1))
u_2 = u_1
print(sys.getrefcount(u_1), sys.getrefcount(u_2))
del u_1
print(sys.getrefcount(u_2))
print('Завершение работы')

