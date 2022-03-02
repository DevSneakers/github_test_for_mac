# 문자열 거꾸로 출력
def rprint(n):
    if len(n) < 1:
        return ""
    else:
        return rprint(n[1:]) + n[0]

print(rprint("abc"))