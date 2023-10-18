import re

while True:
    print("Введите строку")
    s= input()

    if s == '':
        print("Пустая строка")
        exit()
    else:
        if re.match(r"[^\\<>/|?*\"]+\.(txt|doc|docx|odt|rtf)", s):
            print(s, "- является файлом")
