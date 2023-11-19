import re
import os

# Минимальное кол-во слов для предложения
print("Введите кол-во слов")
try:
    min_words = int(input())
except ValueError:
    print("Введено не целое число")
    exit()

# Путь до файла
path = './listochki/predlozhenie_zadanie2.txt'

# Условие если файла нет
if not os.path.exists(path):
    print("Файла нет")
    exit()

# Чтение файла и всех его строк
with open(path) as file:
    strk = file.readline()

# Передаёт предложения в переменную, которые разделяются, если в конце предложения стоит !/?/.
predlozheniya = re.split(r"[!?.]", strk)

path2 = './listochki/result_zadanie2.txt'

if not os.path.exists(path2):
    print("Файла нет")
    exit()


# Записываются предложения в новый файл
a = ''
for i in predlozheniya:
    if len(i.split()) > min_words:
        a += i
        with open("./listochki/result_zadanie2.txt", 'w') as file:
            file.write(a)
        print(i.split())

