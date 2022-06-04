"""Генератор паролей 1"""

import random


def generate_password(length):
    s = [str(i) for i in range(2, 10)]
    s.extend([chr(i) for i in range(ord('a'), ord('z')) if i not in [ord('l'), ord('i'), ord('o')]])
    s.extend([chr(i) for i in range(ord('A'), ord('Z')) if i not in [ord('L'), ord('I'), ord('O')]])
    random.shuffle(s)
    ps = ''
    for _ in range(length):
        ps += random.choice(s)
    return ps

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')