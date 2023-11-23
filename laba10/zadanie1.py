from timeit import timeit

bbl_sort = """
from random import randint

# Cортировка пузырьком
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
    return arr

# Ввод рандомных элементов в массив
bbl_arr = [randint(0, 1000) for x in range(100)]
bubble_sort(bbl_arr)
"""

std_sort = """
from random import randint
# Ввод рандомных элементов в массив
rand_arr = [randint(0, 1000) for x in range(100)]
# Сортировка
rand_arr.sort()
"""

print(f"Время сортировкой методом пузырька: {timeit(bbl_sort, number=100)/100}")
print(f"Время сортировкой со стандартной сортировкой: {timeit(std_sort, number=100)/100}")