"""Интересные числа"""

s, f = int(input()), int(input())

print(*filter(lambda n: all(map(lambda x: x!=0 and n%x==0, map(int, str(n)))), range(s, f+1)))