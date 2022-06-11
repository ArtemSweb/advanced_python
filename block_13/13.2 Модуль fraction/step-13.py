"""Упорядоченные дроби"""

from fractions import Fraction as F

numbers = set()

for i in range(2, int(input()) + 1):
    for j in range(1, i):
        numbers.add(F(j, i))
        
print(*sorted(numbers), sep='\n')
