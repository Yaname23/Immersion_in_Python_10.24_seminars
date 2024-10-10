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
RICH = decimal.Decimal(5000000)
PERS_RICH = decimal.Decimal(10) / decimal.Decimal(100)
PERS = decimal.Decimal(15) / decimal.Decimal(1000)
PERS_BONUS = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = 50
MIN_REMOV = 30
MAX_REMOV = 600
COUNT_OPER = 3

account = decimal.Decimal(0)
count = 0
while True:
    command = input(f'Пополнить - "{CMD_DEP}", Снять - {CMD_WITH}, Выйти - {CMD_EXIT}: ')
    if command == CMD_EXIT:
        print(f'Возьмите карту. Счет карты {account} y.e.')
        break
    if account > RICH:
        percent = account * PERS_RICH
        account -= percent
        print(f'Удержан налог на богатство 10%, что соответствует {percent}y.e.')
        print(f'Итого на карте осталось {account}')
    if command in (CMD_DEP, CMD_WITH):
        amount = 1
        while amount % 50 != 0:
            amount = int(input('Введите сумму, кратную 50: '))
    if command ==  CMD_DEP:
        account += decimal.Decimal(amount)
        count += 1
        print(f'Пополнение карты на  {amount}y.e., \nБаланс счёта {account}')
    elif command == CMD_WITH: # нужно немного доработать, баланс уходит в минус
        withdr_pers = amount * PERS
        withdr_pers = (MIN_REMOV if withdr_pers < MIN_REMOV else MAX_REMOV if withdr_pers > MAX_REMOV else withdr_pers)
        if amount + withdr_pers >= account:
            count += 1
            account -= (amount + withdr_pers)
            print(f'Снятие с карты {amount}y.e. комиссия за снятие составит {withdr_pers}y.e., \nБаланс счёта {account}')
        else:
            print(f'Недостаточно денег на счету. Для снятия: {amount} y.e. \n  Комиссия составит: {withdr_pers} y.e.\nБаланс счёта: {account}')

    if count and count  % COUNT_OPER == 0:
            bonus_pers = account * PERS_BONUS
            account += bonus_pers
            print(f'Начислен бонус в размере {PERS_BONUS}%, что составляет {bonus_pers}y.e. за {COUNT_OPER} операцию по счёту' )
            print(f' Баланс Вашего счёта: {account} y.e.')


        



