#include<stdio.h>

int main()
{
    int age = 0;

    printf("나이 입력 : ");
    scanf("%d",&age);

    int time = 0;

    printf("사용시간 입력 : ");
    scanf("%d", &time);

    if(age >= 20)
        printf("이용 요금은 %d 원 입니다.\n", time*1000);
    else
        printf("이용 요금은 %d 원 입니다.\n", time*700);

    return 0;
}