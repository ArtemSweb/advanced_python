"""Операции над дробями"""

from fractions import Fraction as F

n1, n2 = input(), input()

print(f'{n1} + {n2} = {F(n1) + F(n2)}')
print(f'{n1} - {n2} = {F(n1) - F(n2)}')
print(f'{n1} * {n2} = {F(n1) * F(n2)}')
print(f'{n1} / {n2} = {F(n1) / F(n2)}')
