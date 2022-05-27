import random

lst = []

while len(lst) != 7:
	nmb = random.randint(1, 49)
	if nmb not in lst:
		lst.append(nmb)

print(*sorted(lst))	