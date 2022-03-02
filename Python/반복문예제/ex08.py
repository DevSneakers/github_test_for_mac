# 두 자연수를 사용자 입력받아 j부터 k까지 짝수합을 구하는 프로그램
j = int(input("J 입력 : "))
k = int(input("K 입력 : "))
i = 0
while j <= k:
    if j % 2 == 0:
        i += j
    j += 1
print(i)