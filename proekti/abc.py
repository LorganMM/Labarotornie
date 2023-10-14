import random, timeit

arr = [random.randint(0, 100) for i in range(100)]


def bubble_sort(arr):
    a = 0
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                a += 1
    print("кол-во перестановок пузырьком ", a)
    return arr


def insertion_sort(arr):
    b = 0
    for i in range(0, len(arr) - 1):
        tmp = arr[i]
        j = i - 1
        while j > 0 and tmp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp
        b += 1
    print("кол-во перестановок вставкой ", b)
    return arr


def selection_sort(arr):
    c = 0
    for i in range(0, len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
        c += 1
    print("кол-во перестановок выборкой ", c)
    return arr


bubble_time = timeit.default_timer()
print(bubble_sort(arr))
print("Время пузырька в мс - ", timeit.default_timer() - bubble_time)
selection_time = timeit.default_timer()
print(selection_sort(arr))
print("Время выборкой в мс - ", timeit.default_timer() - selection_time)
insertion_time = timeit.default_timer()
print(insertion_sort(arr))
print("Время вставкой в мс - ", timeit.default_timer() - insertion_time)
