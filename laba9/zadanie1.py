import os

# Указание пути к файлу
path = './listochki/vector_zadanie1.txt'

if not os.path.exists(path):
    print("Отсутствует файл")
    exit()
# Открытие файла
with open(path) as file:
    vtr = [float(x) for x in file.readline().split(',')]

# Определение кол-ва удалений
print("Введите сколько раз нужно удалить числа")
del_nums = 0
try:
    del_nums = int(input())
except ValueError:
    print("Введено не целое число")


# Функция по удалению элемета
def del_vec_nums(vector: list, amount_del: int):
    # Проверка на то, подходит ли кол-во удалений под условие
    if amount_del < 0 or amount_del > len(vector):
        print("Введено некорректное кол-во удалений! Оно должно быть больше 0 и меньше кол-ва элементов в векторе")
        return
    else:
        # Создание цикла, который удаляет последние элементы в векторе amount_del-раз
        for i in range(amount_del):
            vector.pop()
        return vector


result = del_vec_nums(vtr, del_nums)

path2 = './listtochki/result_zadanie1.txt'

if not os.path.exists(path2):
    print("Файл отсутствует")
    exit()

# Вывод ответа в отдельный файл
with open("./listochki/result_zadanie1.txt", 'w') as file:
    file.writelines(str(result).replace("[", "", 1).replace("]", "", 1))


print(result)
