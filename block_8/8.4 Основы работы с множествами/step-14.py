"""Все 10 цифр"""

s = input()+input()

print('YES') if len(set(s))==10 else print('NO')