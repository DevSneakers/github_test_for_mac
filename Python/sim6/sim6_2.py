# 실습 2
A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54]
num = A[0]
i = 1

while i < len(A):
    if A[i] > num:
        num = A[i]
    i += 1

print(num)