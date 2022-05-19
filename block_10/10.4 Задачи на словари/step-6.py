"""Телефонная книга"""

dct = {}
for _ in range(int(input())):
    phone, name = input().split()
    dct.setdefault(name.lower(), []).append(phone)

for _ in range(int(input())):
    print(*dct.get(input(). lower(), ['абонент не найден']))