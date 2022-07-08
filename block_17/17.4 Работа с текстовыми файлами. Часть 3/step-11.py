"""Подарок на новый год"""

with open('class_scores.txt', encoding='utf-8') as inputFile, open('new_scores.txt', 'w', encoding='utf-8') as outputFile:
    for line in inputFile:
        name, score = line.split()
        score = int(score) + 5
        if score > 100:
            score = 100
        print(name, score, file=outputFile)