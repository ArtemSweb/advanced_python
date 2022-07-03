"""Общая стоимость"""

file = open('prices.txt',  encoding='utf-8')
sm = 0

for line in file.readlines():
	arr = line.split()
	sm += int(arr[1]) * int(arr[2])

print(sm)

file.close()