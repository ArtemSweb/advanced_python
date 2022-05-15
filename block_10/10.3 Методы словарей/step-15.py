"""Самое редкое слово 🌶️"""
lst = [i.strip('.,;:-?!()') for i in input().lower().split()]

result = {}

for word in lst:
    result[word] = result.get(word, 0) + 1

print(sorted(i for i in result if result[i]==min(result.values()))[0])
