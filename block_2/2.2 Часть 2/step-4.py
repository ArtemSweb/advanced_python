"""Сдвиг в развитии"""

arr = [int(i) for i in input().split(' ')]
print(arr[-1], *arr[:-1])