"""Максимальный в области 2 🌶️"""

#Строим матрицу по входным данным
n = int(input())
arr = [[int(i) for i in input().split(' ')] for _ in range(n)]
maximum = arr[0][0]

for i in range(n):
    for j in range(len(arr[i])):
        if (i>=j and i <= n-1-j) or (i <= j and i >= n-1-j):
            if maximum < arr[i][j]:
                maximum = arr[i][j]

print(maximum)
