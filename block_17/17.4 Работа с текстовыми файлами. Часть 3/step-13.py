"""Конкатенация файлов 🌶️"""


for _ in range(int(input())):
    with open(input(), encoding='utf-8') as getFile, open('output.txt', 'w', encoding='utf-8') as putFile:
        putFile.write(getFile.read())
