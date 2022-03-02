# 십진수 n을 이진수로 변환하는 프로그램
def rbinary(n):
    if n == 0:
        return ""
    else:
        return rbinary(n // 2) + str(n % 2)

print(rbinary(10))