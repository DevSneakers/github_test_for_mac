# 표준 체중
'''
def std_weight(height, gender):
    if gender == '남자':
        return height**2 * 22
    else:
        return height**2 * 21

weight = std_weight(1.75, '남자')
print(weight)'''

def std_weight(height, gender):
    if gender == '남자':
        return height * height * 22
    else:
        return height * height * 21
    
height = 175
gender = '남자'
weight = round(std_weight(height/100, gender), 2)
print('키 {}cm {}의 표준 체중은 {}kg 입니다.'.format(height, gender, weight))