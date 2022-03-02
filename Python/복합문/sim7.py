# 덧셈문제 10개 출제 후 정답 판단, A,B는 100이하 랜덤 양수
import random

for i in range(10):
    A = int(random.randint(1, 100))
    B = int(random.randint(1, 100))
    n = int(input("{0} + {1} = ".format(A, B)))
    if n == (A + B):
        print('정답')
    else:
        print('오답')