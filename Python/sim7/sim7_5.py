# sim7_5.py
list1 = []
# 내장함수 사용
for j in range(1,6):
    list1.append(('*'* j))

for i in list1:
    print(i.rjust(5))

# 간단한 포맷팅
for i in range(1, 6):
    print("{:>5}".format('*'*i))

# end 사용
j = 1
for i in range(4, -1, -1):
    print(' ' * i, end = '')
    print('*' * j)
    j += 1