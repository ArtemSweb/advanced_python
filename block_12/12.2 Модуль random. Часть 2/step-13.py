"""Генератор паролей 1"""


def generate_password(length):
    s = [i for i in range(2, 10)]
    s.extend([chr(i) for i in range(ord('a'), ord('z')) if i not in [ord('l'), ord('i'), ord('o')]])
    s.extend([chr(i) for i in range(ord('A'), ord('Z')) if i not in [ord('L'), ord('I'), ord('O')]])
    
    return s

def generate_passwords(count, length):
    arr = []
    for _ in range(count):
        arr.append(generate_password(length))
    return arr

n, m = int(input()), int(input())

print(*generate_passwords(n, m))