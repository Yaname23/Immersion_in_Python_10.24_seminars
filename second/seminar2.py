#задача


num = int(input('введите целое число : '))
num2 = num
bin_num = ''
oct_num = ''
#step = True
while num:
    if num % 2 == 0:
        bin_num = str('0') + bin_num
        num //= 2
    else:
        bin_num = str('1') + bin_num

    num //= 2
print(bin_num)
print((bin(num2)))
print('------------вариант 2-----------')
# BASE_BIN  = 2
# BASE_OCT = 8

number = int(input('введите число: '))
base = int(input('ВВедите систему счисления: '))
original_number = number
result_number = ''
while number:
    result_number = str(number%base) + result_number
    number //= base
print(f'Число {original_number} в {base}-ичной системе счисления будет: {result_number} ')
print(bin(original_number)[:2] if base == 2 else oct(original_number)[2:])