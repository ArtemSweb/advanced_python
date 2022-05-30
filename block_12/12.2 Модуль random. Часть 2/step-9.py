import random


blt = set()

while len(blt) < 100:
    blt.add(random.randrange(1000000, 10000000))

print(*blt, sep='\n')