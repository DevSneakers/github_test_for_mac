# 실습 4
'''
num = input("숫자 입력 : ")
i = 0
if len(num)%2 == 1:
    while i < len(num)//2:
        if num[i] == num[-(i+1)]:
            i += 1
            if i == len(num)//2:
                print(True)
        else:
            print(False)
            break
else:
    while i < len(num)//2:
        if num[i] == num[-(i+1)]:
            i += 1
            if i == len(num)//2:
                print(True)
        else:
            print(False)
            break
'''
num = int(input("입력 : "))
tmp = num
pal = 0
while tmp != 0:
    pal *= 10
    pal += tmp % 10
    tmp = tmp // 10
if num == pal:
    print(True)
else:
    print(False)