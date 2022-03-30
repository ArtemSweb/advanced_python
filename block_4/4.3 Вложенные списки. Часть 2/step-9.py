"""Список по образцу 2
[[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]]"""

n = int(input())
arr = []

for i in range(1, n+1):
    arr.append([j for j in range(1, i+1)])

print(*arr, sep='\n')