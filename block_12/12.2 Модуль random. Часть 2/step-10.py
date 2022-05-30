import random


lst = [item for item in input()]
random.shuffle(lst)
print(*lst, sep='')

