# n 입력받아 n보다 작은 소수 출력
n = int(input("50이하 n 입력 : "))
for i in range(2, n + 1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        print(i)