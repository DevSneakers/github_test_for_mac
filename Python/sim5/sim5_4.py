# 실습 4 : 코로나 감염확률 계산
var1 = input("단체 모임을 자주 합니까? (y or n) : ")
var2 = input("손을 자주 씻습니까? (y or n) : ")
var3 = input("마스크를 끼고 외출합니까? (y or n) : ")
per = 0

if var1 == 'y':
    per += 30
    if var2 == 'y':
        per += 5
        if var3 == 'y':
            per += 2
        else:
            per += 20
    else:
        per += 40
        if var3 == 'y':
            per += 2
        else:
            per += 20
else:
    per += 10
    if var2 == 'y':
        per += 5
        if var3 == 'y':
            per += 2
        else:
            per += 20
    else:
        per += 40
        if var3 == 'y':
            per += 2
        else:
            per += 20

print("감염 확률 : %d %%" %per)