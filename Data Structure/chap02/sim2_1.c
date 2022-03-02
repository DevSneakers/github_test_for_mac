#include <stdio.h>

int factorial(int n)
{
    printf("factorial(%d)\n", n);
    if(n <= 1)
        return 1;
    else
        return (n * factorial(n-1));
}

int factorial_iter(int n)
{
    int k, v = 1;
    for (k = n; k > 0; k--){
        v *= k;
    }
    return v;
}

int main()
{
    printf("%d\n", factorial(3));

    printf("%d\n", factorial_iter(3));

    return 0;
}