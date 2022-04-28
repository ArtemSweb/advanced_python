"""Встречалось ли число раньше?"""

lst = input().split(' ')
m = set()

for i in lst:
	if i.lstrip('0') in m:
		print('YES')
	else:
		m.add(i)
		print('NO')
