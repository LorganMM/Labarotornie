print("Введите сумму цифр в трёхзначном числе: ")
a = int(input())
if a < 1:
    print("Число не подходит")
    exit()
if a > 27:
    print("Сумма цифр, привышает максимальную сумму (9+9+9 = 27)")
    exit()
counter = 0
for i in range(100, 1000):
    i1 = int(i / 100)
    i2 = int((float(i / 100) - i1) * 10)
    i3 = int((float(i / 10) - int(i / 10)) * 10)
    if (i3 + i2 + i1) == sum:
        counter += 1
        print(counter)
