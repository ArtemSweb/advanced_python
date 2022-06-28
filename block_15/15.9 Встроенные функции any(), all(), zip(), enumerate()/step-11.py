"""Корректный IP-адрес"""

address = input().split('.')

print(all(map(lambda x: x.isdigit() and int(x) < 256, address)))
