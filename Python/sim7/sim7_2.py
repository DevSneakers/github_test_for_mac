# 실습 2
exclude_num = int(input("제외할 숫자 입력 : "))
for i in range(1, 101):
    if i % exclude_num != 0:
        print(i)