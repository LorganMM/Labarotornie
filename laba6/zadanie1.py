list1 = []
list2 = []

print("Введите размеры векторов")

try:
    arr_sz = int(input())

except ValueError:
    print("Введено не целое число")
    exit()

if arr_sz == 0:
    print("Размер не может быть равным 0")
    exit()

if arr_sz < 0:
    print("Размер не может быть меньше 0")
    exit()


def inp_arr(arr):
    a = 0
    n = 0
    while a < arr_sz:
        n += 1
        print("Введите ", n, " элемент")

        try:
            arr.append(int(input()))
            a += 1
        except ValueError:
            print("Введено не целое число")
            exit()
    return arr


print("Вводится первый веткор")
list1 = inp_arr(list1)

print("Вводится второй вектор")
list2 = inp_arr(list2)

print("Первый вектор: ", list1)
print("Второй вектор: ", list2)

comp = sum(map(lambda x, y: x * y, list1, list2))

print(comp)
