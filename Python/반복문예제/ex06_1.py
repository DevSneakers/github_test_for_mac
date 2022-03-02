# 입력받은 자연수(n)의 모든 약수를 출력
n = int(input("자연수 입력 : "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)