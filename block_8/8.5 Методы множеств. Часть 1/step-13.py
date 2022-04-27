"""Количество слов в тексте"""

s = input().lower().split()

for i in range(len(s)):
	s[i] = s[i].strip('.,;:-?!')

print(len(set(s)))