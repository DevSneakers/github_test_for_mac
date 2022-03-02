# 숫자 입력받고 짝홀수 판단 프로그램 / 음수 입력 시 탈출
while True:
    n = int(input("숫자 입력 : "))
    if n <= 0:
        break
    elif n % 2 == 0:
        out = '짝수'
    else:
        out = '홀수'
    print("{0}은 {1} 입니다.".format(n, out))