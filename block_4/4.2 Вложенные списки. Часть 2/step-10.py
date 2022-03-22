"""Треугольник Паскаля 1 🌶️"""
import math

def pascal(n):
    arr = []
    for i in range(n+1):
        arr.append(int(math.factorial(n)/(math.factorial(i)*math.factorial(n-i))))
    
    return arr

print(pascal(int(input())))