"""Три слова"""

s1, s2, s3 = input().split(' ')

print('YES') if set(s1) == set(s2) and set(s2) == set(s3) else print('NO')