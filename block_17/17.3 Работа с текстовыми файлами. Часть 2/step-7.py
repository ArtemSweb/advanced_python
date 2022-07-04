"""Переворот строки"""

with open('text.txt', encoding='utf-8') as file:
    lines = file.readline()
    print(lines[::-1])