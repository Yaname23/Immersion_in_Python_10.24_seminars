# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"
a = int(frac1[0])
b = int(frac1[2])
c = int(frac2[0])
d = int(frac2[2])
z= int(b *d)
ch = int ((z / b * a) + (z / d * c))
ch2 = int(a * c)
z2 = int(b * d)

print(f'Сумма дробей: ',str(ch) + '/' + str(z))
print(f'Произведение дробей: ',str(ch2) + '/' + str(z2))

fr_summ = Fraction(a, b) + Fraction (c, d)
fr_mult = Fraction(a, b) * Fraction (c, d)
print(f'Сумма дробей: ', fr_summ)
print(f'Произведение дробей: ', fr_mult)
