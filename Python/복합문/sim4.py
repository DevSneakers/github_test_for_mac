# 숫자를 입력받고 약수를 출력
def divisor(n):
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)
    return div

while True:
    n = int(input("숫자 입력 : "))
    if n <= 0:
        break
    else:
        print(divisor(n))