#print('Python', 'Java', 'JavaScript', sep=' vs ')#, end = '?')
#print('무엇이 더 재밌을까요?')
'''
import sys
print('Python', 'Java', file = sys.stdout)
print('Python', 'Java', file = sys.stderr)'''

# 시험 성적
#scores = {'수학':0, '영어':50, '코딩':100}
#for subject, score in scores.items():
    #print(subject, score)
    #print(subject.ljust(8), str(score).rjust(4), sep = ':')

# 은행 대기 순번표
#001, 002, ...
#for num in range(1, 21):
#    print('대기번호 : ' + str(num).zfill(3))
'''
answer = input('아무 값이나 입력 : ')
print('입력한 값은 ' + answer + '입니다.')'''
'''
# 빈 자리는 빈공간, 오른쪽 정렬, 총 10자리 확보
print("{0: >10}".format(500))

# 양수일 때 +, 음수일 때 -
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸 _ 채움
print("{0:_<+10}".format(500))

# 3자리마다 콤마
print("{0:,}".format(100000000))

# 3자리마다 콤마, +- 부호
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))

# 3자리마다 콤마, 부호, 자릿수 확보, 빈자리는 ^
print("{0:^<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 표시 (소수점 3자리)
print("{0:.3f}".format(5/3))
'''

# 파일 입출력
'''
score_file = open("score.txt", "w", encoding = "utf8")
print("수학 : 0", file = score_file)
print("수학 : 50", file = score_file)
score_file.close()'''
'''
score_file = open("score.txt", 'a', encoding = "utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()'''

# pickle
import pickle
'''
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30,"취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile의 정보를 file에 저장
profile_file.close()'''
'''
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()'''

#with
'''
with open("profile.pickle", 'rb') as profile_file:
    print(pickle.load(profile_file))'''
'''
with open("study.txt", 'w', encoding = "utf8") as study_file:
    study_file.write("파이썬을 공부하고 있어요")'''

with open("study.txt", 'r', encoding = "utf8") as study_file:
    print(study_file.read())