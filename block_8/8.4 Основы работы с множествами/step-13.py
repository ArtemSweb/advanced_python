"""Неповторимые цифры"""

s = input()

print('YES') if len(s) == len(set(s)) else print('NO')