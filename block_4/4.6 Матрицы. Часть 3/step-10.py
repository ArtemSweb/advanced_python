"""Заполнение спиралью 😈😈"""

n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
x, y, dx, dy = 0, 0, 0, 1

for i in range(n * m):
    matrix[x][y] = i + 1
    if matrix[(x + dx) % n][(y + dy) % m] != 0:
        dx, dy = dy, -dx
    x, y = x + dx, y + dy

[print(*row) for row in matrix]