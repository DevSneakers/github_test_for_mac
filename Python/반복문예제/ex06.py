# 입력받은 자연수(n)의 모든 약수를 출력
n = int(input("자연수 입력 : "))
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1