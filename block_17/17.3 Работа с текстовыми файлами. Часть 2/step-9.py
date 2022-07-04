"""Длинные строки"""

with open('lines.txt') as file:
    lines = [line.strip() for line in file.readlines()]
    maxLen = max(map(len, lines))
    print(*filter(lambda x: len(x) == maxLen, lines), sep='\n')