print("Введите длины 3 сторон: ")
a = int(input())
b = int(input())
c = int(input())
if (a + b > c) and (b + c > a) and (a + c > b):
    print("Треугольник существует")
else:
    print("Треугольник не существует")

if a ** 2 + b ** 2 < c ** 2:
    print("Тупоугольный")
if a ** 2 + b ** 2 > c ** 2:
    print("Остроугольный")
if a ** 2 + b ** 2 == c ** 2:
    print("Прямоугольный")
