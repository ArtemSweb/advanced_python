"""Заполнение 3"""

n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
            matrix[i][i] = 1
            matrix[i][n - 1 - i] = 1

[print(*row) for row in matrix]