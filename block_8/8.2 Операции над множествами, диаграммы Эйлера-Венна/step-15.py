"""Книги на прочтение 🌶️"""

n,m,k,x,y,z,t,a = [int(input()) for i in range(8)]

book1 = n + m - x - t
book2 = m + k - y - t
book3 = k + n - z - t

# только две книги
only_two = book1 + book2 + book3

# только одну книгу
s = (n - book1 - book3 - t) + (m - book1 - book2 - t) + (k - book2 - book3 - t)

# ничего не прочитали
null = a - s - book1 - book2 - book3 - t

print(s)
print(only_two)  
print(null)  