# 2 - 9 사이의 자연수를 입력받아 구구단 출력
n = int(input("자연수 입력 : "))
for i in range(1, 10):
    print("{0} * {1} = {2}".format(n, i, n * i))