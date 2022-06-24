"""Интересная сортировка-1"""


lst = input().split()

def getSum(num):
	n = [int(i) for i in num]
	return sum(n)

result = sorted(lst, key = getSum)

print(*result)