"""Заполнение диагоналями 🌶️"""

n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
ttl = 1

for k in range(n*m):
    for i in range(n):
        for j in range(m):
            if i+j == k:
                matrix[i][j] = ttl
                ttl += 1

[print(*row) for row in matrix]