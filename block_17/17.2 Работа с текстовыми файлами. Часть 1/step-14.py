"""Сумма двух-1"""

file = open('numbers.txt',  encoding='utf-8')
res = 0

for elem in file:
	res += int(elem)

print(res)

file.close()

#через map

file = open('numbers.txt',  encoding='utf-8')

print(sum(map(int, file)))

file.close()
