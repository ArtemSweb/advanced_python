"""Тайный друг 🌶️"""
import random


lst_1 = [input() for _ in range(int(input()))]
lst_2 = lst_1.copy()

while len(lst_1) > 0:
    elem = lst_1[0]
    chc = random.choice(lst_2)
    if chc != elem:
        print(f'{elem} - {chc}')
        lst_2.remove(chc)
        lst_1.remove(elem)