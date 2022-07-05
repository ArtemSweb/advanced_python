"""Random name and surname"""

from random import choice

with open('first_names.txt',) as fName, open('last_names.txt',) as sName:
    listFirst = [elem.rsplit() for elem in fName.readlines()]
    listSecond = [elem.rsplit() for elem in sName.readlines()]
    for _ in range(3):
        print(*choice(listFirst), *choice(listSecond))