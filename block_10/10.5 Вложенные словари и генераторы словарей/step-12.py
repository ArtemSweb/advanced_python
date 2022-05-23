words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {word: [ord(elem) for elem in word] for word in words}
#вывод не требуется по условиям задачи
print(result)