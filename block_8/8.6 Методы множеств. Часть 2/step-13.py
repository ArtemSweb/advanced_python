"""Количество совпадающих"""


s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

s1 = set(s1)
s2 = set(s2)

s3 = s1 & s2

print(len(s3))