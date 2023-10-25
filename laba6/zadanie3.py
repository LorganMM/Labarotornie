mas = []

print("Введите размер массива")
try:
    arr_sz = int(input())
except ValueError:
    print("Введено не целое число")
    exit()

if arr_sz <= 0:
    print("Размер массива не может быть равным 0 или меньше 0")
    exit()

a = 0
n = 0
while a < arr_sz:
    n += 1
    print("Введите ", n, " элемент")
    try:
        mas.append(int(input()))
        a += 1
    except ValueError:
        print("Введено не целое число")
        exit()

asw = {mas[i]: mas.count(mas[i]) for i in range(len(mas))}
if list(asw.values()).count(max(asw.values())) == 1:
    print("Мода массива =", list(asw.keys())[list(asw.values()).index(max(asw.values()))])
else:
    print("Моды массива не существует")