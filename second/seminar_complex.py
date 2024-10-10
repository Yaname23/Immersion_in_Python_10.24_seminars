# напишите программу, которая решает квадратные уровнения ...

from math import *

a, b, c = 1, -6, 13
d = b ** 2 - 4 * a * c
d = complex(d)
print(d)
x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a)
print(x1)
print(x2)