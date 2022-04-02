"""Обмен столбцов"""

n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split(' ')] for _ in range(n)]
k, f = [int(i) for i in input().split()]

for i in matrix:
    i[k], i[f] = i[f], i[k]

for row in matrix:
    print(*row)