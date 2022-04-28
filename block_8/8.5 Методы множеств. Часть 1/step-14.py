"""Встречалось ли число раньше?"""

lst = [int(i) for i in input().split()]
m = set()

for i in lst:
	print('YES') if i in m else print('NO')
	m.add(i) 
