"""Общие цифры"""


n = int(input())
a = [{int(_) for _ in input()} for i in range(n)]
s = set.intersection(*a)  

print(*sorted(s))