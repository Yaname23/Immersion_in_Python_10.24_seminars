#Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представленеи
#функции bin и oct используйте для проверки своего результата, не для решения

BIN = 2
OCT = 8

num = int(input('Введите целое число: '))

for div in (BIN, OCT):
    result: str = ''
    test_num: int = num
    while test_num > 0:
        result = str(test_num % div) + result
        test_num //= div
    print(f'For {div=} {result=}')

print(f'Двоичное число {bin(num)}, восьмеричное число {oct(num)}')