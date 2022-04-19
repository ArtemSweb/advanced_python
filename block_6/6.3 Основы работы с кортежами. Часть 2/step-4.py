from functools import reduce
numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)

print(reduce(lambda x, y: x * y, numbers))


# или в цикле
# prod = 1
# for i in numbers:
# 	prod *= i

# print(prod)