#include <stdio.h>

// Print a number in binary using n bits
void printBinary(unsigned int num, int n)
{
    for (int i = n - 1; i >= 0; i--)
    {
        printf("%u", (num >> i) & 1u);
    }
}

int main()
{
    unsigned int dividend, divisor;
    unsigned int Q, M;
    int A = 0;
    int n = 0;

    printf("Enter dividend: ");
    scanf("%u", &dividend);

    printf("Enter divisor: ");
    scanf("%u", &divisor);

    if (divisor == 0)
    {
        printf("Division by zero is not allowed.\n");
        return 0;
    }

    // Find required number of bits
    unsigned int temp = dividend;

    do
    {
        n++;
        temp = temp / 2;
    } while (temp > 0);

    // Include divisor's bit length too
    temp = divisor;
    int mBits = 0;

    do
    {
        mBits++;
        temp = temp / 2;
    } while (temp > 0);

    if (mBits > n)
        n = mBits;

    Q = dividend;
    M = divisor;

    printf("\nInitial values:\n");

    printf("A = ");
    printBinary(A, n);

    printf("  Q = ");
    printBinary(Q, n);

    printf("  M = ");
    printBinary(M, n);

    printf("\n");

    for (int i = 0; i < n; i++)
    {
        printf("\n----- Step %d -----\n", i + 1);

        // Step 1: Combined left shift of A and Q
        unsigned int leftmostBit = Q / (1u << (n - 1));

        A = A * 2 + leftmostBit;
        Q = (Q * 2u) % (1u << n);

        printf("After left shift:\n");

        printf("A = ");
        printBinary(A, n);

        printf("  Q = ");
        printBinary(Q, n);

        printf("\n");

        // Step 2: Subtract M
        A = A - (int)M;

        printf("After subtraction: A = %d\n", A);

        // Step 3: Restore if negative
        if (A < 0)
        {
            A = A + (int)M;
            printf("Negative! Restore A.\n");
        }
        else
        {
            Q = Q + 1;
            printf("Positive! Set Q0 = 1.\n");
        }

        printf("Final A = ");
        printBinary(A, n);

        printf("  Q = ");
        printBinary(Q, n);

        printf("\n");
    }

    printf("\n===== RESULT =====\n");
    printf("Quotient = %u\n", Q);
    printf("Remainder = %d\n", A);

    return 0;
}