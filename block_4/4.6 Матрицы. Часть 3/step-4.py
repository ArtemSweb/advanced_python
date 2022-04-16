"""Заполнение 2"""

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    cnt = i
    for j in range(m):
        matrix[i][j] = cnt+1
        cnt +=n

[print(*row) for row in matrix]
