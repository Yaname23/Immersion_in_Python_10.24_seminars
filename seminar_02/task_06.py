#Напишите программу банкомат. Начальная сумма равно 0
# Допустимые действия: пополнить, снять, выйти
# сумма пополнения и снятия кратны 50
# Процент за снятие - 1,5% от суммы снятия, но не больше 600 и не менее 30
# после каждой 3й операции пополнения или снятия начисляются проценты - 3%
# нельзя снять больше чем на счете
# при превышении суммы в 5млн, вычитать налог на богатство 10% перед каждой операцией
# Любое действие выводит сумму денег

import decimal

CMD_DEP = 'n'
CMD_WITH = 'c'
CMD_EXIT = 'b'
RICH = decimal.Decimal(5_000_000)
PERS_RICH = decimal.Decimal(10) / decimal.Decimal(100)
PERS = decimal.Decimal(15) / decimal.Decimal(1000)
PERS_BONUS = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = 50
MIN_REMOV = 30
MAX_REMOV = 600


account = decimal.Decimal(0)
count = 0
while True:
    command = input(f'Пополнить - "{CMD_DEP}", Снять - {CMD_WITH}, Выйти - {CMD_EXIT}')
    if command == CMD_EXIT:
        print(f'Возьмите карту. Счет карты {account} y.e.')
        break
    elif account > RICH:
        percent = account * PERS_RICH
        account -= percent
        print(f'Удержан налог на богатство {PERS_RICH} в размере {percent}y.e.')
        print(f'Итого на карте осталось {account}')

        



