LIMIT = 120
ATTENTION = 'Внимание! '
name = input('твое имя? ')
age = int(input('Твой возраст? '))
text = ATTENTION + 'Хоть тебе и осталось ' + str(100 - age) +\
    ' до ста лет, но длина строки на должна превышать ' + str(LIMIT) +\
    ' символов. '
print(text)