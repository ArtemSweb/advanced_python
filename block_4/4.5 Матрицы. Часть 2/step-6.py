"""Зеркальное отображение"""

n = int(input())
matrix = [[int(i) for i in input().split(' ')] for _ in range(n)]

#Вот и все =)
matrix.reverse()

for row in matrix:
    print(*row)
