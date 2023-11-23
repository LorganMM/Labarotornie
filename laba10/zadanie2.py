import os.path

path = "./listochki/zadanie2.txt"
if not os.path.exists(path):
    print("Файла нет")
    exit()

# Открваем файл и читаем строки (используем encoding, чтобы выводилось на русском)
with open(path, encoding='utf-8') as file:
    words = file.readlines()

# Сортировка
words.sort(reverse=True, key=lambda x: x.count('а'))

print(words)
