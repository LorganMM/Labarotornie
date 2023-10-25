print("Введите размеры матрицы в виде M * K и K * N")

print("Введите M: ")
try:
    M = int(input())
except ValueError:
    print("Введено не целое число")
    exit()

print("Введите K: ")
try:
    K = int(input())
except ValueError:
    print("Введено не целое число")
    exit()

print("Введите N: ")
try:
    N = int(input())
except ValueError:
    print("Введено не целое число")
    exit()

if M <= 0 or K <= 0 or N <= 0:
    print("Число должно быть больше 1")
    exit()

mat1 = [[0 for i in range(M)] for j in range(K)]
mat2 = [[0 for i in range(M)] for j in range(K)]


def inp_mat(matrix):
    n = 0
    for i in range(M):
        for j in range(K):
            n += 1
            print("Введите ", n, " элемент: ")
            try:
                matrix[i][j] = int(input())
            except ValueError:
                print("Введено не целое число")
                exit()
    return matrix


print("Создание первой матрицы...")
mat1 = inp_mat(mat1)

print("Cоздание второй матрицы...")
mat2 = inp_mat(mat2)

print("Первая матрица: ", mat1)
print("Вторая матрица: ", mat2)

matrix_comp = [[0 for i in range(M)] for j in range(K)]
for i in range(M):
    for j in range(K):
        matrix_comp[i][j] = sum(mat1[i][a] * mat2[a][j] for a in range(K))

print("Произведение матриц: ", matrix_comp)
