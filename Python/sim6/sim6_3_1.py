# 실습 3
n1, n2 = input("두 개의 정수 입력 : ").split()
n1 = int(n1)
n2 = int(n2)
num1 = []
num2 = []

i = 1
n = 0
while min(n1,n2) >= i:
    if n1 % i == 0:
        num1.append(i)
    if n2 % i == 0:
        num2.append(i)
    i += 1

length = min(len(num1), len(num2))


# while문을 사용한 최대공약수
while n < length:
    if len(num1) == length:
        if num1[n] in num2:
            result = num1[n]
            n += 1
        else:
            n += 1
    elif num2[n] in num1:
        result = num2[n]
        n += 1
    else:
        n += 1

# for문을 사용한 최대공약수
'''for j in range(0,length):
    if len(num1) == length:
        if num1[j] in num2:
            result = num1[j]
    else:
        if num2[j] in num1:
            result = num2[j]'''
            
print("최대 공약수 : {}".format(result))