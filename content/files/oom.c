#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MB 10485760

int main(int argc, char *argv[]) {
    void *b = NULL;
    int c = 0;

    while(1) {
        b = (void *) malloc(MB);
        if (!b) {
            break;
        }

        memset(b, 1, MB);
        printf("Allocating %d MB\n", (++c * 10));
    }

    exit(0);
}
