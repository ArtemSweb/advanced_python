"""Умножение матриц 🌶️"""

n, m = [int(i) for i in input().split()]
mtx_1 = [[int(j) for j in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
mtx_2 = [[int(j) for j in input().split()] for _ in range(m)]

res_mtx = [[0] * k for i in range(n)]

for i in range(n):
    for j in range(k):
        num = 0
        for l in range(m):
            num += mtx_1[i][l] * mtx_2[l][j]
        res_mtx[i][j] = num

[print(*row) for row in res_mtx]