#include <iostream>

int main() {
    int score = 82;

    if (score >= 90) {
        std::cout << "S" << std::endl;
    } else if (score >= 80) {
        std::cout << "A" << std::endl;
    } else if (score >= 70) {
        std::cout << "B" << std::endl;
    } else if (score >= 60) {
        std::cout << "C" << std::endl;
    } else {
        std::cout << "D" << std::endl;
    }

    return 0;
}