# n의 팩토리얼을 재귀를 사용해 구하라
def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1) * n

print(fact(5))