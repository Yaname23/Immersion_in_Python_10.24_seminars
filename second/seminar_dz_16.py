
# BASE_BIN  = 2
# BASE_OCT = 8
num = 255
number = num
hexadecimal_digits = "0123456789ABCDEF"  # Строка с шестнадцатеричными цифрами
hexadecimal_number = ""

while number > 0:
    remainder = number % 16  # Получаем остаток от деления на 16
    hexadecimal_digit = hexadecimal_digits[remainder]  # Получаем шестнадцатеричную цифру
    hexadecimal_number = hexadecimal_digit + hexadecimal_number  # Добавляем цифру в начало шестнадцатеричного числа
    number //= 16  # Выполняем целочисленное деление на 16

print("Шестнадцатеричное представление числа:", hexadecimal_number)
print(f'Проверка результата:', hex(num))