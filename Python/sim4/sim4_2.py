# 실습 2 : PC방 요금 계산
age = int(input("나이를 입력하세요 : "))
time = int(input("사용 시간을 입력하세요 : "))

if age >= 20:
    print("이용 요금은 %d 입니다." %(time*1000))
else:
    print("이용 요금은 %d 입니다." %(time*700))