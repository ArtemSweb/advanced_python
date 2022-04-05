"""Ходы коня"""

x, y = list(input())
x, y = 'abcdefgh'.index(x), 8 - int(y)

arr = [['.*'[abs((x - j) * (y - i)) == 2] for j in range(8)] for i in range(8)]
arr[y][x] = 'N'

[print(*row) for row in arr]