"""Обратный порядок"""

with open('data.txt', encoding='utf-8') as file:
    lines = file.readlines()
    lines.reverse()
    for elem in lines:
        print(elem.rstrip('\n'))