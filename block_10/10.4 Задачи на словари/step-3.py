"""Анаграммы 2"""

s1 = sorted([i for i in input().lower() if i.isalpha()])
dct1 = dict(zip(range(len(s1)), s1))

s2 = sorted([i for i in input().lower() if i.isalpha()])
dct2 = dict(zip(range(len(s2)), s2))

print('YES') if dct1 == dct2 else print('NO')
