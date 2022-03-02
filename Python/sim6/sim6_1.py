# 실습 1
num = 100

while True:
    n = int(input("정수 입력 : "))
    num -= n
    if num <= 0:
        break
    print("{}은 0보다 큰 숫자입니다.".format(num))

a = int(input("정수 a입력 : "))
b = int(input("정수 b입력 : "))
result = 0
for i in range(a, b+1):
    result += i
print(result)