# 실습 3
import math
from copy import copy
n1, n2 = input("두 개의 정수 입력 : ").split()
n1 = int(n1)
n2 = int(n2)
num1 = 1
i = 2
result = math.gcd(n1, n2)
n = 1

while n >= 1:
    if i == 10:
        i = 2
    elif n1 % i == 0 and n2 % i == 0:
        num1 *= i
        i += 1
    elif n1 % i != 0 and n2 % i != 0:
        n = 0
    else:
        i += 1
        
print(result)
print(num1)
