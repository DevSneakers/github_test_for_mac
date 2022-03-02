# 실습 3 : 사분면 구하기
x = int(input("x좌표를 입력 : "))
y = int(input("y좌표를 입력 : "))

if x > 0:
    if y > 0:
        print("1 사분면")
    else:
        print("4 사분면")
else:
    if y > 0:
        print("2 사분면")
    else:
        print("3 사분면")