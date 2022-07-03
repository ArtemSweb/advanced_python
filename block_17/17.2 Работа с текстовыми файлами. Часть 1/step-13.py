"""Случайная строка"""
import random

file = open('lines.txt', encoding='utf-8')
print(random.choice(file.readlines()))

file.close()
