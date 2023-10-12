print("Введите число N:")
N = int(input())
if N < 0:
    print("N - неправильное число")
print("Введите число M:")
M = int(input())
if M < 0:
    print("M - неправильное число")

if len(str(abs(N))) > len(str(abs(M))):
    print("В числе N больше цифр")
elif len(str(abs(N))) == len(str(abs(M))):
    print("Числа равны")
else:
    print("В числе M больше цифр")
