year = int(input("연도 입력 : "))

if year % 4 != 0:
    print('{}년은 평년입니다.'.format(year))
elif year % 100 != 0:
    print('{}년은 윤년입니다.'.format(year))
elif year % 400 == 0:
    print('{}년은 윤년입니다.'.format(year))
else:
    print('{}년은 평년입니다.'.format(year))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            out = '윤년'
        else:
            out = '평년'
    else:
        out = '윤년'
else:
    out = '평년'

print('{}년은 {}입니다.'.format(year, out))