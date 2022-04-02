"""Максимум в таблице"""

n, m = int(input()), int(input())
arr = [[int(i) for i in input().split(' ')] for _ in range(n)]

ind = [0, 0]
max = arr[0][0]

for i in range(n):
    for j in range(m):
        if max < arr[i][j]:
            max = arr[i][j]
            index_max = arr[i].index(max)
            ind = [i, index_max]

print(*ind)