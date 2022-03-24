"""Разбиение на чанки 🌶️"""

def chunked(text, chunk):
    arr = [x for x in text.split(' ')]
    new_arr = list()
    for i in text:
        while len(arr) != 0:
            new_arr.append(arr[:chunk])
            del arr[:chunk]


    return new_arr

print(chunked('a b c d e f r g b', 1))