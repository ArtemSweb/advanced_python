"""Магический квадрат 🌶️"""

n = int(input())
matrix = [[int(i) for i in input().split(' ')] for _ in range(n)]

flag = 'YES'
m = sum(matrix[0])
digits = [i for i in range(1, n ** 2 + 1)]

#проверка равенства сумм чисел по строчно
for i in range(n):
    if sum(matrix[i]) != m:
        flag = 'NO'
        break

#
for i in range(n):
    for j in range(n):
        if matrix[i][j] in digits:
            digits.remove(matrix[i][j])
    if i == n - 1 and j == n - 1 and digits != []:
        flag = 'NO'
        break

#
for j in range(n):
    result = 0
    for i in range(n):
        result += matrix[i][j]
        if i == n - 1 and result != m:
            flag = 'NO'
            break

print(flag)