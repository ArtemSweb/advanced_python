numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {key: sorted([value for value in range(1, key+1) if key % value == 0]) for key in numbers}
#вывод не требуется по условиям задачи
print(result)