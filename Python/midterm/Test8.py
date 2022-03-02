id_num = input("주민등록번호 입력 : ")
year = int(id_num[:2])
month = int(id_num[2:4])
idx_sex = id_num[7]

if int(id_num[0]) > 2:
    is_adult = '성인'
elif (21-year) >= 20:
    is_adult = '성인'
elif (21-year) == 19:
    if month <= 11:
        is_adult = '성인'
    else:
        is_adult = '미성년'
else:
    is_adult = '미성년'

if idx_sex == '1' or idx_sex == '3':
    sex = '남자'
elif idx_sex == '2' or idx_sex == '4':
    sex = '여자'
else:
    sex = '성별 입력 오류'

print('{} {}입니다.'.format(is_adult, sex))