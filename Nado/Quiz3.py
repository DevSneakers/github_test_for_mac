
url = 'http://google.com'
str1 = url.replace('http://','')
# print(str1)
str1 = str1[:str1.index('.')]
# print(str1)
password = str1[:3] + str(len(str1)) + str(str1.count('e')) + '!'
print('{}의 비밀번호는 {}입니다.'.format(url, password))