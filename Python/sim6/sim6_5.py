# 실습 5 : 피보나치수열
n = int(input("숫자 입력 : "))
j = [1, 1]
i = 2
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while i <= n:
        j.append((j[i-2]+j[i-1]))
        i+= 1
print(j[(n-1)])

n = int(input())
i = 2
before = 1
now = 1
while i < n:
    tmp = before + now
    before = now
    now = tmp
    i += 1
if n <= 2:
    print(1)
else:
    print(now)