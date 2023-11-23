def palid(symbols, usl):
    for i in range(len(symbols)):
        del_el = symbols.pop()
        if not del_el == s[int(len(s) / 2 + i + usl)]:
            print("Не палиндром")
            exit()
    print("Палиндром")


print("Введите от 3 символов")
s = list(input())

if len(s) < 3:
    print("Введено меньше 3 символов")
    exit()

symb = list()
for i in range(int(len(s) / 2)):
    symb.append(s[i])

even_or_odd = len(s) % 2

palid(symb, even_or_odd)
