"""След матрицы"""

n = int(input())
arr = [input().split(' ') for _ in range(n)]
res = 0

for i in range(len(arr)):
    res += int(arr[i][i])

print(res)

