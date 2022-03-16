"""Камень, ножницы, бумага"""

timur , ruslan = input(), input()

if timur.lower() == ruslan.lower():
    print('ничья')
elif timur == 'ножницы' and ruslan == 'бумага':
    print('Тимур')
elif timur == 'бумага' and ruslan == 'камень':
    print('Тимур')
elif timur == 'камень' and ruslan == 'ножницы':
    print('Тимур')
else:
    print("Руслан")
