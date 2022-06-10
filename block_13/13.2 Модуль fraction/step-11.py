"""Сумма дробей 2"""

from fractions import Fraction as F
from math import factorial as fct


n = int(input())
res = 0

for i in range(1, n+1):
    res += F(1, fct(i))

print(res)