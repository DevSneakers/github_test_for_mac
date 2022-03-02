# 함수
'''def open_account():
    print("새로운 계좌 생성")

def deposit(balance, money):
    print("입금 완료. 잔액은 {}원 입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance >= money:
        print('출금 완료. 잔액은 {}원'.format(balance - money))
        return balance - money
    else:
        print('출금 불가. 잔액 {}원'.format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print('수수료 {}원, 잔액 {}원'.format(commission, balance))'''

'''
# 기본 값
# def profile(name, age, main_lang):
#     print('이름 : {}\t나이 : {}\t주 사용언어 : {}'.format(name, age, main_lang))
    
# profile('유재석', 20, '파이썬')
# profile('강호동', 25, '자바')

# 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age = 17, main_lang = '파이썬'):
    print('이름 : {}\t나이 : {}\t주 사용언어 : {}'.format(name, age, main_lang))

profile('유재석')
profile('강호동')'''

# 키워드 값
'''
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = '유재석', main_lang = '파이썬', age = 20)
profile(main_lang = '자바', age = 25, name = '강호동')
'''
# 가변 인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {}\t나이 : {}\t".format(name, age), end = '')
#     print(lang1, lang2, lang3, lang4, lang5)
'''
def profile(name, age, *language):
    print("이름 : {}\t나이 : {}\t".format(name, age), end = '')
    for lang in language:
        print(lang, end = ' ')
    print()

profile('유재석', 20, 'Python', 'Java', 'C', 'C++', 'C#', 'JavaScript')
profile('강호동', 25, 'Kotlin', 'Swift', '', '', '')
'''
# 지역변수, 전역변수

gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간의 gun 사용
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {}'.format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {}'.format(gun))
    return gun

print('전체 총 : {}'.format(gun))
gun = checkpoint_ret(gun, 2)
print('남은 총 : {}'.format(gun))