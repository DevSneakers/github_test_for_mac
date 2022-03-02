# sim7_3.py
a = int(input("처음 숫자 입력 : "))
b = int(input("마지막 숫자 입력 : "))
s = 0

for i in range(a, b+1):
    s += i
    
print(s)