DEFAULT = 42
num = int(input('введите уровень или ноль для значения по умолчнию: '))
level = num or DEFAULT
print(level)
print('-----------------------')

name = input('как вас зовут? ')
if name:
    print('Привет, ' + name)
else:
    print('Анонимус, привествую')
print('-----------------------')
# работа с коллекцией
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
while data:
    print(data.pop())
print('-----------------------')