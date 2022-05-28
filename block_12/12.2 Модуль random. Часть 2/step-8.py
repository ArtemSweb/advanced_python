import random

matrix = [  [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

new_lst = sum(matrix, [])
random.shuffle(new_lst)
matrix = [[new_lst[i * 4 + j] for j in range(4)] for i in range(4)]

print(matrix)
