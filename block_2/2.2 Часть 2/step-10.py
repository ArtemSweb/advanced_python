"""Кремниевая долина 🌶️🌶️"""

n = int(input())
arr = []

for i in range(1, n + 1):
    virus = ["a","n","t","o","n"]
    word = input()

    for j in word:
        if j == virus[0]:
            del virus[0]
        if len(virus) == 0:
            arr.append(i)
            break

print(*arr)
