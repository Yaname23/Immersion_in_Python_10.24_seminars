x = int("42")
y = int(3.1415)
z = int('hello', base=30)
print(x, y, z, sep='\n')
print('-----------------------')

import sys

STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    num *= STEP
print('-----------------------')

nums = 7_901_123_4567
print((nums))
print('-----------------------')
number = 2 ** 16 -1
b = bin(number)
o = oct(number)
h = hex(number)
print(b, o, h)
print('-----------------------')

