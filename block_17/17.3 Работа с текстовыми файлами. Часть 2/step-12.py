"""Статистика по файлу"""

with open('file.txt', encoding='utf-8') as file:
    countLines = 0
    countWords = 0
    countLetters = 0
    for line in file.readlines():
        countLines += 1
        countWords += len(line.split())
        countLetters += len([elem for elem in line if elem.isalpha()])


print(f'Input file contains:\n{countLetters} letters\n{countWords} words\n{countLines} lines ')
