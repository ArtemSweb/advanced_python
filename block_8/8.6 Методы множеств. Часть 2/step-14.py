"""Общие числа"""

s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
s3 = s1 & s2

print(*sorted(s3))