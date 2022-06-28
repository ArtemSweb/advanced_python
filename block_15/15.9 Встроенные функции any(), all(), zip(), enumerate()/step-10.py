
abscissas = [float(elem) for elem in input().split()]
ordinates = [float(elem) for elem in input().split()]
applicates = [float(elem) for elem in input().split()]
r = 2

print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= r**2, zip(abscissas, ordinates, applicates))))