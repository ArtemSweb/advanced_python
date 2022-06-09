from decimal import *


num = Decimal(input())
lst = sorted([int(elem) for elem in str(num) if elem.isdigit()])

print(lst[0]+lst[-1])
