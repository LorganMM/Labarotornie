import os
from operator import itemgetter

path = "./listochki/zadanie3.txt"
if not os.path.isfile(path):
    print("файла нет")
    exit()

# Открывает и читает все строки
with open(path) as file:
    lines = file.readlines()

names_and_ages = list(map(lambda x: x.split(), lines))

# Сортировка 0 - имена, 1 - возраст
sort = sorted(names_and_ages, key=itemgetter(0, 1))

print(sort)
