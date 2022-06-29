"""Хороший пароль"""

s = input()

truePassword = all([any(map(lambda x: x.isdigit(), s)), any(map(lambda x: x.isupper(), s)), any(map(lambda x: x.islower(),s)), len(s)>6])

print('YES' if truePassword else "NO")
