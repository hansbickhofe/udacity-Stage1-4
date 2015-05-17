with open('days.txt') as fp:
    for day in iter(fp.readline, ''):
        print(day)
