#include <stdio.h>

int main(void) {
    const char *items[] = {"apple", "banana", "orange"};

    printf("sizeof(items[0]) = %zu\n", sizeof(items[0]));
    printf("sizeof(items)    = %zu\n", sizeof(items));

    int length = sizeof(items) / sizeof(items[0]);
    printf("length           = %d\n", length);

    return 0;
}
