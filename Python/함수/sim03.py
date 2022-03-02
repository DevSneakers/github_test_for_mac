# 별 출력, 인자는 있지만 리턴이 없는 경우
def print_star(n):
    for i in range(n):
        print("*", end = "")
    print("")

print_star(5)
print_star(10)