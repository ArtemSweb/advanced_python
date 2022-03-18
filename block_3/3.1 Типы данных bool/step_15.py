"""Предикат делимости"""

# объявление функции
def func(num1, num2):
    return not num1 % num2 

# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
print('делится' if func(num1, num2) else 'не делится')