def calculator(*args):
    result = 0
    for i in args:
        result += i
    return result

def question():
    count = int(input("숫자를 더 입력하려면 1, 아니면 0을 입력하세요 : "))
    return count
# input
count = 1
num = []
while(count > 0):
    num.append(int(input("계산할 숫자를 입력하세요 : ")))
    count = question()
print(123)