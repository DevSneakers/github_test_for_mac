# 끝말잇기 게임, 틀릴 때까지 계속, 단어 입력 후 입력했던 단어 모두 출력
start = input("끝말잇기 시작 첫 단어 입력 : ")
data = start
print(data)

pre = start
while True:
    new = input("단어 입력 : ")
    if pre[-1] == new[0]:
        pre = new
        data = data + ' -> ' +new
        print(data)
    else:
        print('패배')
        break