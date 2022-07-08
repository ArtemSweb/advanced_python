"""Лог файл 🌶️"""

def get_diff_mins(endTime, startTime):
    t2 = list(map(int, endTime.split(':')))
    t1 = list(map(int, startTime.split(':')))
    return (t2[0]*60 + t2[1]) - (t1[0]*60 + t1[1])

with open('logfile.txt', encoding='utf-8') as logfile, open('output.txt', 'w') as output:
    for fn in logfile:
        name, startTime, endTime = fn.strip().split(', ')
        if get_diff_mins(endTime, startTime) >= 60:
            print(name, file=output)