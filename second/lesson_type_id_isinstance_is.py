# вывод типов данных и id

a = 5
print(type(a), id(a))
a = 'hello world'
print(type(a), id(a))
a = 42.0 * 3.141592 / 2.71828
print(type(a), id(a))
print('-----------------------')
#для сравнения значений с типами
data = 42
print(isinstance(data, int))

data = True
print(isinstance(data, int))

data = 3.14
print(isinstance(data, int))
print('-----------------------')
# is савнение значений между собой
num = 2 + 2 * 2
digit = 36 /6
print(num, 'и',  digit)
print((num == digit))
print(num is digit)

