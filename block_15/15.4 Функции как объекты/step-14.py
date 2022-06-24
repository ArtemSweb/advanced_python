"""квадрат: функция принимает число и возвращает его квадрат;
куб: функция принимает число и возвращает его куб;
корень: функция принимает число и возвращает корень квадратный из этого числа;
модуль: функция принимает число и возвращает его модуль;
синус: функция принимает число (в радианах) и возвращает синус этого числа."""

import math

def sqr(num):
	return num**2

def cube(num):
    return num**3

def root(num):
    return num**0.5

def module(num):
    return abs(num)

def sine(rad):
    return math.sin(rad)

n = int(input())
name = input()

dctFunc = {"квадрат": sqr, "куб": cube, "корень": root, "модуль": module, "синус": sine}

print(dctFunc[name](n))