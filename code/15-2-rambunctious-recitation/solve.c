// c99 -O2 solve.c -o solve
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char const *argv[]) {
    int input[] = {0,14,6,20,1,4};
    const int S = sizeof(input)/sizeof(input[0]);
    const int N = 30000000;

    int* seen = calloc(N, sizeof(int));

    for (int i = 0; i < S; ++i) {
        seen[input[i]] = i + 1;
    }

    int res, x = 0;
    for (int i = S + 1; i < N + 1; ++i) {
        res = x;
        int p = seen[x];
        seen[x] = i;
        x = p ? (i - p) : 0;
    }

    printf("%u\n", res);

    return 0;
}
