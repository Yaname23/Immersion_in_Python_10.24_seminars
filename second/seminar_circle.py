#Напиши программу, которая вычисляе площадь круга и длину окружнсти по введённому деаметру\
#диаметр не превышает 1000 у.е. и точность вычисления должна составлять не менее 42 знаков после запятой
import decimal
from decimal import Decimal
import math

decimal.getcontext().prec = 42 # ограничения, можно не указывть

while True:
    d = int(input('введите диаметр не превышающий 1000 : '))
    if d <= 1000:
        square = Decimal((math.pi * (d ** 2)) / 4)
        circumference = Decimal(math.pi * d)
        print(f'Площадь круг с диаметром {d} равна {square},площадь окружности равна {circumference}')
        quit()
    else:
        result = 'error!'
        print("Введенное число не соответствует запросу, попробуйте снова")
    if result != 'error!':
        break