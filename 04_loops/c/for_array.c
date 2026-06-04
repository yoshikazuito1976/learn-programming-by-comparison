#include <stdio.h>

int main(void) {
    const char *items[] = {"apple", "banana", "orange"};
    int length = 3;

    for (int i = 0; i < length; i++) {
        printf("%s\n", items[i]);
    }

    return 0;
}
