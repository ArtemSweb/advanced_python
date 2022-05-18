"""Словарь синонимов"""

dct = dict([[word for word in input().split(' ')] for _ in range(int(input()))])
s = input()

for key, value in dct.items():
    if key == s:
        print(value)
    if value == s:
        print(key)