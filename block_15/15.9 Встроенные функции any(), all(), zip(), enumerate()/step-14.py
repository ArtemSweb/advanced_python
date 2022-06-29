"""Отличники"""

progress = []
for _ in range(int(input())):  
    progress.append(any(['5' in input().split() for _ in range(int(input()))]))
        
print('YES' if all(progress) else 'NO')