# 실습 1 : 두부게임
tofu = int(input("두부 몇 모? : "))

if tofu <= 0 or tofu > 5:
    print("ERROR) 유효한 숫자를 입력 (1 ~ 5)")
elif tofu == 3:
    print("두부 네 모!")
else:
    print("두부"*tofu)