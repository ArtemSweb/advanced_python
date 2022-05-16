"""Словарь программиста"""

lst = [(input().split(':')) for _ in range(int(input()))]
dct = {elem[0].lower(): elem[1].strip() for elem in lst}


for elem in [input().lower() for _ in range(int(input()))]:
    print(dct.get(elem, 'Не найдено'))
