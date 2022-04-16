"""Сложение матриц"""

n, m = map(int, input().split())
matrix1 = [[int(i) for i in input().split(' ')] for _ in range(n)]
n_str = input()
matrix2 = [[int(i) for i in input().split(' ')] for _ in range(n)]
new_mtx = []

for i in range(n):
	new_arr = []
	for j in range(m):
		new_arr.append(matrix1[i][j] + matrix2[i][j])
	new_mtx.append(new_arr)


[print(*row) for row in new_mtx]