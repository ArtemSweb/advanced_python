import random

lst = random.sample(range(1, 76), 25)
lst[12] = 0

for i in range(len(lst)):
    print(str(lst[i]).ljust(3), end='')
    if i in[4, 9, 14, 19]:
        print()