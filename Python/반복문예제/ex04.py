# 자연수(n)를 입력받아 0부터 n까지 짝수를 출력하는 프로그램
n = int(input('자연수 입력 : '))
i = 0
while i < n:
    if i % 2 == 0:
        print(i)
    i += 1

i = 0
while i < n:
    print(i)
    i += 2

for j in range(0, n, 2):
    print(j)