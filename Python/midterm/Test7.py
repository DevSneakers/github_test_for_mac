time = input("시간 입력 : ")
t = int(time)
hours = int(time[:2])
minutes = int(time[2:])

if hours < 24 and minutes < 60:
    if t >= 0 and t <= 1159:
        AMPM = '오전'
    elif t >= 1200 and t <= 2359:
        AMPM = '오후'
    print('{}시 {}분은 {} 입니다.'.format(hours, minutes, AMPM))
else:
    print('잘못 입력하였습니다.')
