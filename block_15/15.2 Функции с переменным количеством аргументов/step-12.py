

def mean(*args):
    lst = [elem for elem in args if type(elem)== int or type(elem) == float]
    return float(sum(lst)/len(lst)) if len(lst)>0 else float(0)
    

print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))