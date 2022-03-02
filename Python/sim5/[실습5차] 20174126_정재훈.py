# 실습 1 : 배수 구하기
num = int(input("숫자 입력 : "))

if num % 3 == 0:
    if num % 15 == 0:
        out = '15의 배수'
    elif num % 21 == 0:
        out = '21의 배수'
    else:
        out = '15와 21의 배수가 아닌 3의 배수'
else:
    out = '3의 배수가 아닌 수'

print("{}은 {} 입니다.".format(num, out))
