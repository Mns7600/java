#include <stdio.h>
#include <string.h>

#define MAX 1000

int max(int a, int b) {
    return (a > b) ? a : b;
}

void findLCS(const char *x, const char *y) {
    int m = strlen(x);
    int n = strlen(y);
    static int dp[MAX][MAX]; // DP table for LCS lengths

    // Build the LCS table
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else if (x[i - 1] == y[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    int length = dp[m][n];
    char lcs[MAX];
    int index = 0;

    int i = m;
    int j = n;

    // Backtrack to construct the subsequence
    while (i > 0 && j > 0) {
        if (x[i - 1] == y[j - 1]) {
            lcs[index++] = x[i - 1];
            i--;
            j--;
        } else if (dp[i - 1][j] >= dp[i][j - 1]) {
            i--;
        } else {
            j--;
        }
    }

    // Reverse to get the correct order
    for (int left = 0, right = index - 1; left < right; left++, right--) {
        char temp = lcs[left];
        lcs[left] = lcs[right];
        lcs[right] = temp;
    }

    lcs[index] = '\0';

    printf("Length of LCS: %d\n", length);
    printf("Longest Common Subsequence: %s\n", lcs);
}

int main(void) {
    char x[MAX], y[MAX];

    printf("Enter first string: ");
    scanf("%s", x);

    printf("Enter second string: ");
    scanf("%s", y);

    printf("String 1: %s\n", x);
    printf("String 2: %s\n\n", y);

    findLCS(x, y);
    return 0;
}
