# 실습 3 : 사분면 구하기
x = int(input("x좌표를 입력 : "))
y = int(input("y좌표를 입력 : "))

if x > 0 and y > 0:
    print("1사분면")
elif x < 0 and y > 0:
    print("2사분면")
elif x > 0 and y < 0:
    print("4사분면")
else:
    print("3사분면")