# 실습 4 : 코로나 감염확률 계산
var1 = input("단체 모임을 자주 합니까? (y or n) : ")
var2 = input("손을 자주 씻습니까? (y or n) : ")
var3 = input("마스크를 끼고 외출합니까? (y or n) : ")

if var2 == 'n':     # 손을 씻지 않는지 검사
    per = 40
elif var1 == 'y':   # 단체 모임을 갖는지 검사
    per = 30
elif var3 == 'n':   # 마스크를 끼지 않는지 검사
    per = 20
else:               # 모두 아닐 때
    per = 10

print("당신의 감염 확률은 {}% 입니다.".format(per))