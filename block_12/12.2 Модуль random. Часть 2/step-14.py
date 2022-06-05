"""Генератор паролей 2 🌶️"""

import random
import string

# с проверкой пароля на прохождение условия
# def generate_password(length):
#     s = [str(i) for i in range(2, 10)]
#     s.extend([chr(i) for i in range(ord('a'), ord('z')) if i not in [ord('l'), ord('i'), ord('o')]])
#     s.extend([chr(i) for i in range(ord('A'), ord('Z')) if i not in [ord('L'), ord('I'), ord('O')]])
#     random.shuffle(s)
#     ps = ''
#     for _ in range(length):
#         ps += random.choice(s)
#     return ps

# def check_password(password):
#     flag_1 = 0
#     flag_2 = 0
#     flag_3 = 0
#     for i in password:
#         if i.isupper():
#             flag_1 = 1
#         if i.isdigit():
#             flag_2 = 1
#         if i.islower():
#             flag_3 = 1
#     return flag_1 + flag_2 + flag_3 == 3

# def generate_passwords(count, length):
#     lst = []
#     while len(lst)!= count:
#         pswrd = generate_password(length)
#         if check_password(pswrd):
#             lst.append(pswrd)
#     return lst

# n, m = int(input()), int(input())

# print(*generate_passwords(n, m), sep='\n')



#сразу генерировать пароль
us = [i for i in string.ascii_uppercase if i not in 'OI']
ls = [i for i in string.ascii_lowercase if i not in 'ol']
ds = [str(i) for i in range(2, 10)]

lst = us+ls+ds

def generate_password(length):
    res = [random.choice(i) for i in (us, ls, ds)] + [random.choice(lst) for _ in range(3, length)]
    random.shuffle(res)
    return res

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())

for i in generate_passwords(n, m):
    print(*i, sep='')
