"""Подсписки списка 🌶️"""

def listlistlist(d):
    arr = d.split()
    res = [[]]
    for i in range(1, len(arr) + 1):
        for j in range((len(arr) + 1)-i):
            res.append(arr[j:j+i])
    return res

print(listlistlist(input()))
