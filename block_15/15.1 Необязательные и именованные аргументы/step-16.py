
def matrix(row=1, col=0, n=0):
    if row == 1 and not col:
        col = 1
    elif row != 1 and not col:
        col = row
    return [[n]*col for _ in range(row)]


print(matrix(3))