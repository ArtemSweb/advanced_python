"""Значение многочлена 🌶️"""

from functools import reduce

evaluate = lambda c, x: reduce(lambda v, c: c + v * x, map(int, c))
print(evaluate(input().split(), int(input())))