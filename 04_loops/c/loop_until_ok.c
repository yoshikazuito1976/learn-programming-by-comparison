#include <stdio.h>
#include <string.h>

int main(void) {
    char input[100];

    while (1) {
        printf("Type ok: ");
        scanf("%99s", input);

        if (strcmp(input, "ok") == 0) {
            break;
        }

        printf("Try again.\n");
    }

    printf("Finished.\n");

    return 0;
}
