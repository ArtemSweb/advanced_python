"""Максимальный в области 1"""

#Строим матрицу по входным данным
n = int(input())
arr = [[int(i) for i in input().split(' ')] for _ in range(n)]
max = arr[0][0]

for i in range(n):
    for j in range(i+1):
        if max < arr[i][j]:
            max = arr[i][j]

print(max)