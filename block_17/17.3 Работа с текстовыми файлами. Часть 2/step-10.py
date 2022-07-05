"""Сумма чисел в строках"""


with open('numbers.txt', encoding='utf-8') as file:
    for line in file.readlines():
        print(sum([int(elem) for elem in line.split()]))