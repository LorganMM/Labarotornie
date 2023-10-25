print("Введите I строку")
# stroka1 - I строка
stroka1 = input()

print("Введите II строку")
# stroka2 - II строка
stroka2 = input()

stroka1 = set(stroka1)
stroka2 = set(stroka2)
# Замена элементов строки только на уникальные

asw = stroka1.difference(stroka2)
# difference - замена на различные элементы

# Проверка, равен ли поиск универсальных элементов пустоте (set()), если да - различных элементов нет
if asw == set():
    print("Нет различных элементов")
    exit()

print("Элементы из I строки, которых нет во II строке: ", asw)
