"""Поворот матрицы"""

n = int(input())
matrix = [[int(i) for i in input().split(' ')] for _ in range(n)]

matrix.reverse()

for i in range(n):
    for j in range(len(matrix[i])):
        print(matrix[j][i], end = ' ')
    print()
