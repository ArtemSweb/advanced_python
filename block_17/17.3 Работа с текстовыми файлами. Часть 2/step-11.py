"""Сумма чисел в файле"""

with open('nums.txt', encoding='utf-8') as file:
    sm = 0
    for line in file.readlines():
        s = ''
        for elem in line:
            s += elem if elem.isdigit() else " "
        sm += sum([int(elem) for elem in s.split()])
print(sm)
