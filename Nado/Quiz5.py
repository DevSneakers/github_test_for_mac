# 승객 별 운행 소요 시간 5 ~ 50분 사의의 난수
# 소요 시간 5~ 15분 사이의 승객만 매칭
''' 출력 예제
[O] 1번째 손님 (소요시간 : 15분)'''

'''from random import *

time = []

for i in range(50):
    time.append(randint(5, 50))

for i in range(1, 51):
    if time[i-1] < 16:
        ox = 'O'
    else:
        ox = ' '
    print('[{}] {}번째 손님 (소요시간 : {}분)'.format(ox, i, time[i-1]))'''