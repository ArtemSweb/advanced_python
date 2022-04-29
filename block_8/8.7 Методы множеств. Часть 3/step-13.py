"""Урок биологии"""

set1, set2, set3 = (set(int(i) for i in input().split()) for i in range(3))
set4 = set(range(0, 11))

print(*sorted(set4 - (set1 | set2 | set3)))