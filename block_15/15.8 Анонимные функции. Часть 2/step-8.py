
is_num = lambda x: "-" not in x[1:] and x.strip('-').replace('.', '', 1).isdigit()

#для python 3.9
# is_num = lambda s: s.removeprefix('-').replace('.','',1).isdigit()


print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
print(is_num('1-1'))