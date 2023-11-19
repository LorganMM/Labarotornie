import re
import os

# Путь в файл
path = './listochki/text_zadanie4.txt'

# Файла нет
if not os.path.isfile(path):
    print("Файла нет")
    exit()

# Чтение файла
with open('./listochki/text_zadanie4.txt') as file:
    l1 = file.readlines()

path2 = './listochki/result_zadanie4.txt'
if not os.path.exists(path2):
    print("Файла нет")
    exit()

# Запись результата в новый файл
with open('./listochki/result_zadanie4.txt', 'w') as file:
    for i in range(len(l1)):
        if re.match(r"Chapter*", l1[i]):
            file.write((l1[i] + l1[i + 1]).replace("\n", " ") + "\n")

# Вывод ответа
with open('./listochki/result_zadanie4.txt') as file:
    read_res = file.readlines()
print(read_res)
