#1
print(1<=1)
#2
print('Dog'<'dog')
#3
print('fun' in 'refunded')

a = 2
b = 3
c = 'hello'

#4
print((a+b)<(2*a))
#5
print((len(c)-b) == (a/2))

n = 4
answ = 'Y'

#6
print((2<n) and (n<6))
#7
print((2<n) or (n == 6))
#8
print((answ == 'Y') and (answ == 'y'))
#9
print(((n == 2) and (n == 7) or (answ == 'Y')))
#10
print(((2 < n) and (n == 5) or (answ == 'No')))

'''
결과값
1. True
2. True
3. True
4. False
5. False
6. True
7. True
8. False
9. True
10. False
'''