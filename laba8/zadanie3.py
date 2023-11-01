RusToEngDict = {'Привет': 'Hello','Я': "I'm", 'Максим': 'Maksim'} # Русско-английский словарь
EngToRusDict = {'Hello': 'Привет', "I'm": 'Я', 'Maksim': 'Максим'} # Английско-русский словарь

while True:
    print("С какого языка вы хотите перевести? рус/англ")
    lang = input()
    # Выбор русского языка
    if lang == 'рус':
        print("Введите строку на русском")
        rus = input().split(' ')
        rus = [x.capitalize() for x in rus] # Каждое введённое слово начинается с заглавной буквы, а остальные с нижним регистром
        RusToEng = [RusToEngDict.get(x.capitalize()) if RusToEngDict.get(x) else x for x in rus]
        print(RusToEng)
        break
    # Выбор английского языка
    if lang == 'англ':
        print("Введите строку на английском")
        eng = input().split(' ')
        eng = [x.capitalize() for x in eng] # Каждое введённое слово начинается с заглавной буквы, а остальные с нижним регистром
        RusToEng = [EngToRusDict.get(x.capitalize()) if EngToRusDict.get(x) else x for x in eng]
        print(RusToEng)
        break
    else:
        print("Введена неверная команда, попробуйте снова")