
result = {}

for i in range(1, 16):
	result[i] = result.get(i, i**2)
	
#принт по условиям задачи не нужен
print(result)