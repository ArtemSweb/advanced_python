"""На вход программе подается натуральное число n.
Напишите программу, которая выводит первые nn строк треугольника Паскаля."""
import math

def pascal(n):
    arr = []
    for i in range(n+1):
        arr.append(int(math.factorial(n)/(math.factorial(i)*math.factorial(n-i))))
    
    return arr

n = int(input())
for i in range(n):
    print(*pascal(i))