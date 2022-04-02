"""Симметричная матрица"""

n = int(input())
matrix = [[int(i) for i in input().split(' ')] for _ in range(n)]
flag = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != matrix[j][i]:
            flag += 1
            break

print('NO' if flag > 0 else 'YES')   