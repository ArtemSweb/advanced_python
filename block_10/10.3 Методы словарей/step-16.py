"""Исправление дубликатов 🌶️"""

dct, lst= {}, []

for letter in input().split():
    if letter not in lst:
        lst.append(letter)
    else:
        dct[letter] = dct.get(letter, 0) + 1
        lst.append(letter + '_' + str(dct[letter]))

print(*lst)