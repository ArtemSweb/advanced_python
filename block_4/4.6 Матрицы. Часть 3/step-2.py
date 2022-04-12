"""Побочная диагональ"""

n = int(input())
matrix = [['0'] * n for _ in range(n)]

for i in range(n):
    matrix[i][n-i-1] = 1
    for j in range(n):
        if i > n-j-1:
            matrix[i][j] = 2


[print(*row) for row in matrix]
