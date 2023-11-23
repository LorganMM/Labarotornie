import os.path

path = "./listochki/zadanie3.txt"
if not os.path.exists(path):
    print("Файла нет")
    exit()

with open(path, encoding="utf-8") as file:
    lines = file.readlines()

lines = list(map(lambda x: x.split(","), lines))
lines = [[lines[i][x].replace("\n", "").replace(" ", "") for x in range(len(lines[i]))] for i in range(len(lines))]


arr = list()

maxlen = max((len(lines[x]) for x in range(len(lines))))
j = 0
while j < maxlen:
    for i in range(len(lines)):
        if lines[i]:
            arr.append(lines[i].pop(0))
    j += 1

print("очередь: ", ", ".join(arr))