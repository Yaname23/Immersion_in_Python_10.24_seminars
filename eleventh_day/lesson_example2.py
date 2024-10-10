class User:
    def __init__(self, name: str):
        self.name = name
            #принт только в учебных целях. так делать не рекомендуется
        print(f'создал  {self.name = }')

    def __new__(cls, *args, **kwargs):
        isinstance = super().__new__(cls)
        print(f'создал клaсс  {cls }')
        return isinstance

print('Создаём первый раз ')
u_1 = User('Спенглер')
print('Создаём второй раз ')
u_2 = User('Венкман')
print('Создаём третий раз ')
u_2 = User(name='Стэнц')