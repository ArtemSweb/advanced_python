"""Тимур и его команда"""

n, m, k, x, y, z = [int(input()) for _ in range(6)]

total = z + (n-x) + (m - x -y) + (k-y)+ x+y

print(total)