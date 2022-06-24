"""Интересная сортировка-2"""


lst = sorted([int(elem) for elem in input().split()])

def getSum(num):
	n = [int(i) for i in str(num)]
	return sum(n)

result = sorted(lst, key = getSum)

print(*result)