#include<stdio.h>

int main(){
    int dividend, divisor;
    int A = 0, Q, M;
    int n = 0;
    int temp;
    int i;

    printf("Enter dividend: ");
    scanf("%d", &Q);
    printf("Enter divisor");
    scanf("%d", &M);

    if (divisor == 0 || dividend < 0 || divisor < 0)
    {
        printf("Invalid input");
        return 0;
    }

    Q = dividend;
    M = divisor;

    temp = dividend;

    do {
        n++;
        temp = temp/2;
    } while (temp>0);

    for (i = 0; i < n; i++){
        A = A*2 + Q / (1<< (n-1));
        Q = (Q*2)%(1<<n);

        A = A-M;

        if (A<0){
            A = A + M;
        }
        else {
            Q = Q + 1;
        }
    }
    printf("Quotient = %d\n", Q);
    printf("Remainder = %d\n", A);

    return 0;
}