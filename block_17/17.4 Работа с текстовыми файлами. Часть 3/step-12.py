"""Загадка от Жака Фреско 🌶️"""

with open('goats.txt', encoding='utf-8') as goats, open('answer.txt', 'w', encoding='utf-8') as answer:
    lst = []
    for string in goats.read().split('GOATS'):
        lst.append(string.strip('COLOURS').strip('\n').strip(' goat ').split(' goat\n'))
    for c in lst[0]:
        if lst[1].count(c) > len(lst[1]) * 0.07:
            print(f'{c} goat', file=answer)