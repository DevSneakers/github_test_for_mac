# 주 1회 작성 보고서
'''
n주차 주간보고
부서 :
이름 : 
업무 요약 : 
'''
# 1 ~ 50주차 보고서 파일 만들기
'''
report = ['부서', '이름', '업무 요약']
for i in range(1, 51):
    with open("{}주차.txt".format(i), 'w', encoding = "utf8") as report_file:
        report_file.write("- {}주차 주간 보고 -\n".format(i))
        for j in report:
            report_file.write("{} : \n".format(j))
        report_file.close()'''
