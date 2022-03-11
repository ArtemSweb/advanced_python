"""Координатные четверти"""

n = int(input())
coutOne, coutTwo, coutThree, coutFour = [0,0,0,0]

for i in range(n):
    x, y = map(int, input().split(' '))
    if x>0 and y>0:
        coutOne += 1
    elif x<0 and y>0:
        coutTwo += 1
    elif x<0 and y<0:
        coutThree += 1
    elif x>0 and y<0:
        coutFour +=1

print(f'Первая четверть: {coutOne}\nВторая четверть: {coutTwo}\nТретья четверть: {coutThree}\nЧетвертая четверть: {coutFour}')