def invert(string):
    for i in range(len(string)):
        arr.append(s.pop())


print("Введите строку")
s = list(input())

arr = list()
invert(s)
print("Инвертированная строка")
print(''.join(arr))