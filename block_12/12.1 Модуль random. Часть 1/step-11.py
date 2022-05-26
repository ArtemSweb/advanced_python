import random

n = int(input())    # количество попыток

for _ in range(n):
	print('Орел') if random.randint(0,1)==0 else print('Решка')