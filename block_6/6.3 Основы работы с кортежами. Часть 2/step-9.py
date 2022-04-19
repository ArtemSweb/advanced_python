"""Конкурсный отбор"""

n = int(input())
tpl = tuple()
for i in range(n):
    tpl += tuple(input().split()),

for i in tpl:
    print(*i)

print()

for stud in tpl:
    if int(stud[1]) > 3:
        print(*stud) 