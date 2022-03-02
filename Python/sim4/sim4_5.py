# 실습 5 : lucky 7
num = int(input("숫자 입력 : "))
repeat = num//7

if num % 7 == 0:
    print(str(num) * repeat)