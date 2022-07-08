"""Нумерация строк"""

with open('input.txt', encoding='utf-8') as inputFile, open('output.txt', 'w', encoding='utf-8') as outputFile:
    for i, j in enumerate(inputFile, start=1):
        outputFile.write(f'{i}) {j}')
