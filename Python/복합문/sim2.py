# 1단부터 9단까지 모든 구구단 출력
def gugu(n):
    for i in range(1, 10):
        print("{0} X {1} = {2}".format(n, i , n * i))
    print("="*50)

for i in range(2, 10):
    gugu(i)