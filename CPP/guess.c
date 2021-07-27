#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
        srand(time(0));
        int n = rand()%70;
        int x;
        int N = 5;
        printf("[0, 69]\n\n");

        while(x != n && N > 0)
        {
                printf("%d tries left\n", N);
                printf("guess: ");
                scanf("%d", &x);
                if(x > n)
                {
                    printf("too big, like my\n\n");
                }
                if(x < n)
                {
                    printf("too small, like your\n\n");
                }
                N--;
        }
        if(N == 0)
        {
                printf("%d tries left\n", N);
                printf("oonp\n\n");
        }
        else {
                printf("kkk\n\n");
        }
}

