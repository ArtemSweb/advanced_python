"""Таблица умножения"""

n, m = int(input()), int(input())
arr = [[int(i)*int(j) for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end =' ')
    print()
print()

