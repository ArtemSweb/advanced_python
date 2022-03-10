"""Индекс массы тела"""

weight = float(input())
height = float(input())

imt = weight / height**2

if 18.5 <= imt <= 25:
    print('Оптимальная масса')
elif imt < 18.5:
    print('Недостаточная масса')
else:
    print('Избыточная масса')