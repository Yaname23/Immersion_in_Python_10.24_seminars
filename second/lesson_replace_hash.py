#если числа пайтон может изменять, то в строках только через
#специальные операторы
text = 'hello world!'
print(text, id(text))
text = text.replace(' ', '_')
print(text, id(text))
print('-----------------------')
#функция hash
x = 42
y = 'text'
z = 3.1415

print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
#print(hash(my_list))# полуим ошибку, т.к. list изменяемый
print('-----------------------')
