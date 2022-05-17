"""Анаграммы 1"""

s1 = sorted(input())
dct1 = dict(zip(range(len(s1)), s1))

s2 = sorted(input())
dct2 = dict(zip(range(len(s2)), s2))

print('YES') if dct1 == dct2 else print('NO')
