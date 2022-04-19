numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
res_arr = []
for tpl in numbers:
    ttl = sum(tpl) / len(tpl)
    res_arr.append(ttl)

print(res_arr)