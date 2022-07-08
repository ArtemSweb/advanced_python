"""Случайные числа"""

import random


with open('random.txt', 'w', encoding='utf-8') as file:
    count = 25
    while count > 0:
        file.write(f'{random.randint(111,777)}\n')
        count -= 1

