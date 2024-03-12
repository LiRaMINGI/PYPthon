def f(mat):
    det = mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1]) - mat[0][1] * (
                mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) + mat[0][2] * (
                      mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])

    if det == 0:
        return "линейно зависимые"
    else:
        return "Линейно независимые"


# Пример матрицы
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 80]
]

res = f(mat)
print(res)
print("Матрица:")
for row in mat:
    print(row)