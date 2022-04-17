"""Возведение матрицы в степень 🌶️"""

n = int(input())
mtx = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
res_mtx = mtx.copy()

def square_matrix_mult(mtx_1, mtx_2, x):
    res_mtx = [[0] * x for _ in range(x)]
    for i in range(x):
        for j in range(x):
            for q in range(x):
                res_mtx[i][j] += mtx_1[i][q] * mtx_2[q][j]
    return res_mtx
    

for _ in range(m - 1):
    res_mtx = square_matrix_mult(mtx, res_mtx, n)

[print(*row) for row in res_mtx]