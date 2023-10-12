print("Введите число:")
N = int(input())
if N < 0:
    print("Введено неверное число")
    exit()
a = 1
for i in range(1, N + 1):
    a *= i
    print(a)
