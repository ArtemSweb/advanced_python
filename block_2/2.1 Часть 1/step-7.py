"""Переворот числа"""

num = [i for i in input()]

if len(num) == 5:
    print(int(''.join(num[::-1])))
elif len(num) == 6:
    str = num[0] + ''.join(num[-1:0:-1])
    print(int(str))