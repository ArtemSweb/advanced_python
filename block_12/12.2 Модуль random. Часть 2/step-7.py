import random
import string

# var_1
def generate_index_1():
    return f'{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}{random.randint(0,99)}_{random.randint(0,99)}{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}'

print(generate_index_1())

# var_2
def generate_index_2():
    n1, n2 = (random.randrange(100) for _ in range(2))
    s1, s2, s3, s4 = (random.choice(string.ascii_uppercase) for _ in range(4))
    return f'{s1}{s2}{n1}_{n2}{s3}{s4}'

print(generate_index_1())