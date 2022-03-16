"""Орел и решка"""

word = input().split('О')

# в key передаем то по чему ищем(по длинне)
print(len(max(word, key=len)))

