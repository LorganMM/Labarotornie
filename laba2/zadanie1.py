print("Введите M - больший шестизначный номер: ")
M = int(input())
if M < 100000 or M > 999999:
    print("M не шестизначный номер")
    exit()
print("Введите N - наименьший шестизначный номер: ")
N = int(input())
if N < 100000 or N > 999999:
    print("N не шестизначный номер")
    exit()
if N > M:
    print("N должно быть меньше, чем M")
    exit()
count = 0
for numbers in range(N, M + 1):
    n1 = int(numbers / 100000)
    n2 = int((float(numbers / 100000) - n1) * 10)
    n3 = int((float(numbers / 10000) - int(numbers / 10000)) * 10)
    n4 = int((float(numbers / 1000) - int(numbers / 1000)) * 10)
    n5 = int((float(numbers / 100) - int(numbers / 100)) * 10)
    n6 = int((float(numbers / 10) - int(numbers / 10)) * 10)
    if (n1 + n2 + n3) == (n4 + n5 + n6):
        count += 1
        print(count)
