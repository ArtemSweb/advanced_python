"""Стоимость строки"""

str = input()
PRICE = 60

cost = len(str)*PRICE

print(f'{cost//100} р. {cost%100} коп.')

