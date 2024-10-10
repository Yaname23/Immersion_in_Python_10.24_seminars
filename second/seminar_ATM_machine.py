# напишите программу банкомат. Начальная сумма равна 0, допустимые действия: пополнить, снят, выйти,
# сумма пополнения и снятия кратна 50 y.e.,
#  проценнт для снятия 1,5% от суммы снятия, но не менее
# 30 и не более 600 у.е.. поле каждой третей операции пополнения или снятия начисляюся проценты - 3%
# нельзя снять больше чем на счёте
# При привышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией,
# даже оибочной, любое действие выводит сумму денег


count = 0
count2 = 0
rich = count / 100 * 10 / 12

while True:
    active = int (input(" Выберите тип операции - введите цифру: \n 1.Пополнить \n 2.Снять деньги\n 3.Выйти \n "))
    if active == 1:
        replenishment = int (input("введите сумму кратную. 50: \n"))
        if replenishment % 50 == 0:
            count = count + replenishment
            count2 += 1
            if count2 % 3 == 0:
                rl = replenishment / 100 * 3
                count = count -rl
                print(f'произошло списание процентов за количество транзакций в размере {rl}\n')
            print(f'сумма на Вашем счёте: {count}\n')
        else:
            print('введённая сумма не кратна 50, попробуйте ещё раз\n')
        continue
    elif active == 2:
        withdrawal = int (input("при снятии взимается 1,5 % от суммы, но не менее 30 и не более 600 \n введите сумму кратную. 50: \n"))
        if withdrawal % 50 == 0 :
            wd = withdrawal / 100 * 1.5
            if wd < 30:
                wd = 30
                if withdrawal + wd <= count:
                    count = count - withdrawal - wd
                    count2 += 1
                    if count2 % 3 == 0:
                        wdl = withdrawal / 100 * 3
                        count = count - wdl
                        print(f'произошло списание процентов за количество транзакций в размере {wdl}\n')
                    print(f'комиссия за снятие составила: {wd}, сумма на Вашем счёте: {count}\n')
                else:
                    print(" на Вашем счёте недостаточно средств\n")
                    continue
            elif wd > 600:
                wd = 600
                if withdrawal + wd <= count:
                    count = count - withdrawal - wd
                    count2 += 1
                    if count2 % 3 == 0:
                        wdl = withdrawal / 100 * 3
                        count = count - wdl
                        print(f'произошло списание процентов за количество транзакций в размере {wdl}\n')
                    print(f'комиссия за снятие составила: {wd}, сумма на Вашем счёте: {count}\n')
                else:
                    print(" на Вашем счёте недостаточно средств\n")
                    continue
            else:
                if withdrawal + wd <= count:
                    count = count - withdrawal - wd
                    count2 += 1
                    if count2 % 3 == 0:
                        wdl = withdrawal / 100 * 3
                        count = count - wdl
                        print(f'произошло списание процентов за количество транзакций в размере {wdl}\n')
                    print(f'комиссия за снятие составила: {wd}, сумма на Вашем счёте: {count}\n')
                else:
                    print(" на Вашем счёте недостаточно средств\n")
                    continue

        else:
            print('введённая сумма не кратна 50, попробуйте ещё раз\n')
        continue

    elif active == 3:
        print("Сеанс завершён")
        quit()
    else:
        print("неверно указан тип операции, попробуйте снова\n")
        continue

