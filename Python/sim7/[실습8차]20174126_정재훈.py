a = int(input("정수 a입력 : "))
b = int(input("정수 b입력 : "))
result = 0

for i in range(a, b+1):
    result += i
    
print(result)