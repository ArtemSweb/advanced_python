"""Список по образцу 1
[[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]]"""
#не совсем вложенные списки, но подходит под условия
n = int(input())

for i in range(1, n+1):
    print([int(j) for j in range(1, n+1)])