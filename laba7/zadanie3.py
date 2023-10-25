print("Введите I строку: ")
# stroka1 - I строка
stroka1 = input()

print("Введите II строку: ")
# stroka2 - II строка
stroka2 = input()

if stroka1.isdigit() and stroka2.isdigit():
    stroka1 = set(stroka1)
    stroka2 = set(stroka2)
    # Используем set, чтобы строка состояла только из уникальных элементов

    asw = stroka1.intersection(stroka2)
    # stroka1.intersection(stroka2) - поиск общих элементов в строке 1 и в строке 2

    # Проверка, равен ли поиск общих элементов пустоте (set()), если да - общих элементов нет
    if asw == set():
        print("Общих элементов нет")
        exit()

    print("Общие элементы I и II строк = ", asw)

else:
    print("В строках находятся символы")
