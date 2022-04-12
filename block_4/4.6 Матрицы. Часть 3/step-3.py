"""Заполнение 1"""

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
cnt = 1

for i in range(n):
    for j in range(m):
        matrix[i][j] = cnt
        cnt +=1

[print(*row) for row in matrix]