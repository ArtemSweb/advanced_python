"""Больше среднего"""

n = int(input())
arr = [[int(i) for i in input().split(' ')] for _ in range(n)]

for i in arr:
    avr = sum(i)/len(i)
    cnt = 0
    for j in i:
        if j > avr:
            cnt += 1
    print(cnt)
