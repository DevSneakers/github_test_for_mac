# 실습 2 : 가장 큰 수 구하기
n = []
for i in range(1,4):
    n.append(int(input("정수{} 입력 : ".format(i))))

if n[0] > n[1]:
    if n[0] > n[2]:
        print("가장 큰 정수는 {} 입니다.".format(n[0]))
    else:
        print("가장 큰 정수는 {} 입니다.".format(n[2]))
elif n[1] > n[2]:
    print("가장 큰 정수는 {} 입니다.".format(n[1]))
else:
    print("가장 큰 정수는 {} 입니다.".format(n[2]))