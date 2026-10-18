#include <stdio.h>
#include <string.h>

#define D 256
#define Q 101

void rabinKarp(char *pattern, char *text) {
    int m = strlen(pattern);
    int n = strlen(text);
    int p = 0;
    int t = 0;
    int h = 1;

    // Compute hash value for pattern and first text window
    for (int i = 0; i < m - 1; i++)
        h = (h * D) % Q;

    for (int i = 0; i < m; i++) {
        p = (D * p + pattern[i]) % Q;
        t = (D * t + text[i]) % Q;
    }

    // Slide the pattern over the text
    for (int i = 0; i <= n - m; i++) {
        if (p == t) {
            int match = 1;
            for (int j = 0; j < m; j++) {
                if (text[i + j] != pattern[j]) {
                    match = 0;
                    break;
                }
            }

            if (match) {
                printf("Pattern found at index %d\n", i);
            }
        }

        // Update rolling hash for the next window
        if (i + m < n) {
            t = (D * (t - text[i] * h) + text[i + m]) % Q;
            if (t < 0)
                t += Q;
        }
    }
}

int main(void) {
    char text[1000], pattern[100];

    printf("Enter the text: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = '\0';

    printf("Enter the pattern: ");
    fgets(pattern, sizeof(pattern), stdin);
    pattern[strcspn(pattern, "\n")] = '\0';

    rabinKarp(pattern, text);
    return 0;
}