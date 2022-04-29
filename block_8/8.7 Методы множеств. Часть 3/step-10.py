"""Урок информатики"""

set1, set2, set3 = (set(int(i) for i in input().split()) for i in range(3))

print(*sorted(set(set1.intersection(set2).difference(set3)), reverse=True))