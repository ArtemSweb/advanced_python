"""Задача Иосифа Флавия 🌶️🌶️"""

# https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%98%D0%BE%D1%81%D0%B8%D1%84%D0%B0_%D0%A4%D0%BB%D0%B0%D0%B2%D0%B8%D1%8F

# n = int(input())
# k = int(input())

# surv = 0
# for i in range(1, n+1):
#     surv = (surv + k) % i

# print(surv + 1)


#решение через рекурсию

def lastSurv(n, k):
    if n == 1:
        return 1
    else:
        return ((lastSurv(n - 1, k) + k - 1) % n + 1)

print(lastSurv(int(input()), int(input())))