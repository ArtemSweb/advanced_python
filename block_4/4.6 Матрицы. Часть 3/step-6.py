"""Заполнение 4"""

n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][i] = 1
        matrix[i][n - 1 - i] = 1
        if (i < j and i < n-1-j) or (i > j and i > n-1-j):
            matrix[i][j] = 1

[print(*row) for row in matrix]