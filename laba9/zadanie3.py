import os
import re


def transp(mat):
    t_mat = [[0 for _ in range(len(mat))] for k in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            t_mat[j][i] = mat[i][j]
    return t_mat


path = './listochki/matrix_zadanie3'

if not os.path.exists(path):
    print("Файла нет")
    exit()

with open(path) as file:
    strk = file.readlines()

matrix = [i.split() for i in strk]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        try:
            int(matrix[i][j])
        except ValueError:
            print("Тут букова")
            exit()

t_matrix = transp(matrix)

path2 = './listochki/result_zadanie3.txt'

if not os.path.exists(path2):
    print("Файла нет")
    exit()

with open("./listochki/result_zadanie3.txt", 'w') as file:
    for i in t_matrix:
        for j in i:
            file.write(j)
        file.write("\n")

print(matrix)
print(t_matrix)
