"""Вывести матрицу 1"""

rows, cols = int(input()), int(input())
arr = [['']*cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        arr[i][j] = input()

for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end =' ')
    print()
