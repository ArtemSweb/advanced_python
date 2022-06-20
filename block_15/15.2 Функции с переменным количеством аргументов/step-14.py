def print_products(*args):
    lst = [elem for elem in args if type(elem) == str and len(elem)>0]
    if len(lst)>0:
        for i, val in enumerate(lst, 1):
            print(f'{i}) {val}')
    else:
        print('Нет продуктов')




print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')