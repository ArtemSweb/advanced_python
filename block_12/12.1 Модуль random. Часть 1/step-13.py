import random

length = int(input())
lst = []

for _ in range(length):
	lst.append(chr(random.randint(65, 90))) if random.randint(0,1)==0 else lst.append(chr(random.randint(97, 122)))

print(*lst, sep='')