"""Заполнение 5 🌶️"""

n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1


[print(*row) for row in matrix]
