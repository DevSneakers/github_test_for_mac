# 실습 4 : 생년월일 출력
id_num = input("주민등록번호 앞자리를 입력 : ")
year = int(id_num[:2])

if year > 3:
    print("생일은 19%s 년 %s 월 %s 일 입니다." %(id_num[:2], id_num[2:4], id_num[4:6]))
else:
    print("생일은 20%s 년 %s 월 %s 일 입니다." %(id_num[:2], id_num[2:4], id_num[4:6]))