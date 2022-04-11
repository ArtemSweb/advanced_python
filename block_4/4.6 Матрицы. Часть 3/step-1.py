"""Шахматная доска"""

n, m = [int(i) for i in input().split()]
matrix = [['.'] * m for _ in range(n)]

for i in range(n):
    if i == 0 or i % 2 == 0:
        for j in range(1, m, 2):
            matrix[i][j] = '*'
    else:
        for j in range(0, m, 2):
            matrix[i][j] = '*'

[print(*row) for row in matrix]