# 실습 3 : 만 나이 출력
def func():
    print('='*50)

input_list = ['현재년', '현재월', '현재일', '출생년', '출생월', '출생일']
list1 = []

for i in input_list:
    list1.append(int(input("{}을 입력 : " .format(i))))

func()
print("오늘 날짜 : {}년 {}월 {}일".format(list1[0], list1[1], list1[2]))
print("생년월일 : {}년 {}월 {}일".format(list1[3], list1[4], list1[5]))
func()

if list1[1] >= list1[4]:        # 현재월, 출생월 비교
    if list1[2] >= list1[5]:    # 현재일, 출생일 비교
        age = list1[0] - list1[3]
    else:
        age = list1[0] - list1[3] - 1
else:
    age = list1[0] - list1[3] - 1

print("만 나이 : {}".format(age))

if age >= 19:
    print("성인입니다.")
else:
    print("미성년입니다.")