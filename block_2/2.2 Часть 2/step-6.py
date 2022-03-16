"""Произведение чисел"""
#получаем кол-во чисел в массиве
n = int(input())
arr = []

#пишем числа в массив
for i in range(n):
    arr.append(int(input()))

#получаем число для определения произведения
multiplication = int(input())
flag = False

#считаем и сравниваем
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if multiplication==arr[i]*arr[j]:
            flag = True
            break

print("НЕТ" if flag != True else"ДА")