# sim7_4.py
chart = []

for i in range(1,31):
    chart.append(i)

for j in chart:
    if j < 10:
        print(' ', end = '')
        if j == 1:
            print(' '*16, end = '')
    if j == 4 or j == 11 or j == 18 or j == 25:
        print('')
        if j == 4:
            print(' ', end = '')
    print(' ',j, end = '')