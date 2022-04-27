"""Уникальные символы 2"""

unic = set()

for _ in range(int(input())):
    s = input().lower()
    for elem in s:
        unic.add(elem)

print(len(unic))