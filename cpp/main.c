#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double max(double a, double b)
{
    double r;
    if(a > b)
    {
        r = a;
    }
    else {
        r = b;
    }
    return r;
}

double cube(double n)
{
    printf("lmao age^3 = ");
    double r = n*n*n;
    return r;
}

int main()
{
    printf("howst old R yuo?\n");

    int a = 420;
    int age = 69;
    char name[] = "GONDRO";

    printf("it is %s at %d\n", name, age);
    printf("%f\n", cube(age));
    printf("%f\n", max(a,age));
    return 0;
}

