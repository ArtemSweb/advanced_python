"""Заполнение змейкой"""

n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
cnt = 1

for i in range(n):
    for j in range(m):
        matrix[i][j] = cnt
        cnt+=1

    if i % 2 != 0:
        matrix[i].reverse()
    

[print(*row) for row in matrix]
