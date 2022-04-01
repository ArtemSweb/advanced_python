"Суммы четвертей"

n = int(input())
arr = [[int(i) for i in input().split(' ')] for _ in range(n)]
top, right, bottom, left = 0, 0, 0, 0



for i in range(n):
    for j in range(len(arr[i])):
        if (i<j and i < n-1-j):
            top += arr[i][j]
        if (i < j and i > n-1-j):
            right += arr[i][j]
        if (i>j and i > n-1-j):
            bottom += arr[i][j]
        if (i > j and i < n-1-j):
            left += arr[i][j]

print(f"""Верхняя четверть: {top}
Правая четверть: {right}
Нижняя четверть: {bottom}
Левая четверть: {left}""")
