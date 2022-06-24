athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

n = int(input())

def getBySortVariant(tpl):
	return tpl[n-1]

sortAthletes = sorted(athletes, key=getBySortVariant)
for athlete in sortAthletes:
	print(*athlete)