tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = []
for i in range(len(tuples)):
	new_arr = []
	for j in tuples[i]:
		new_arr.append(j)
	new_arr = new_arr[:-1]
	new_arr.append(100)
	new_tuples.append(tuple(new_arr))


print(new_tuples)