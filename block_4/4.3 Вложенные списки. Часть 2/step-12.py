"""Упаковка дубликатов 🌶️"""
from itertools import groupby

def createArr(s):
    arr = s.split(' ')
    new_arr = []
    
    for i, j in groupby(arr):
        new_arr.append(list(j))
    return new_arr

print(createArr(input()))
