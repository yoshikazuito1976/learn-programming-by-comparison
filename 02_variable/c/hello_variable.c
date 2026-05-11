#include <stdio.h>

int main(void) {
    char name[] = "yoshikazu";
    int age = 48;
    double height = 170.5;

    printf("%s\n", name);
    printf("%d\n", age);
    printf("%f\n", height);

    printf("Hello, %s\n", name);
    printf("Age: %d\n", age);
    printf("Height: %.1f\n", height);

    return 0;
}
