"""Роскомнадзор запретил букву а 🌶️🌶️"""

s = input()
text = f'{s} запретил букву'

arr = list(set(text.replace(" ",'')))
arr.sort()

for i in arr:
    print(f'{text} {i}')
    text = text.replace(i, '').strip().replace('  ', ' ')
