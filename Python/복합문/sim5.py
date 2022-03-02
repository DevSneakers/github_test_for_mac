# n을 입력받아 1과 n사이에 완전수 출력
n = int(input("숫자 입력 : "))

for i in range(1, n+1):
    num = 0
    for j in range(1, i):
        if i % j == 0:
            num += j
    if num == i:
        print(i)