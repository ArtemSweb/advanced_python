"""Секретное слово"""

s = input()
n = int(input())
dct = dict([[word.strip() for word in input().split(':')] for _ in range(n)])
#переворот ключ/значение
dct = {int(value): key for key, value in dct.items()}

for elem in s:
    print(dct[s.count(elem)], end='')

