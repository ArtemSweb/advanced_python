"""Страны и города"""

dct = dict()

for _ in range(int(input())):
    s = input().split()
    dct[s[0]] = s[1:]

for _ in range(int(input())):
    city = input()
    for key, value in dct.items():
        if city in value:
            print(key)