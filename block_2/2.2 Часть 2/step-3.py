"""Назад, вперёд и наоборот"""

arr = [int(i) for i in input().split(' ')]

for i in range(0, len(arr)-1 , 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]

print(*arr)