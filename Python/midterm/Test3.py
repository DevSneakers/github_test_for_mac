list1 = []
for i in range(1,6):
    list1.append(int(input("정수{} 입력 : ".format(i))))

avg = sum(list1)/len(list1)

print(list1)
print('Maximum:{} Minimum:{} Average:{}'.format(max(list1),min(list1),avg))