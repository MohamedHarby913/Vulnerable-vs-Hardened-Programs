#include <stdio.h>
#include <string.h>

// this function is to read the input buffer
void read_input(char *buffer, int size) {
    printf("Enter your username to access your account\n");
    gets(buffer);
}
// this function is to print the output buffer
void print_buffer(char *buffer, int size) {
    printf("Welcome ");
    for (int i = 0; i < size; i++) {
        printf("%c", buffer[i]);  // Buffer over-read happens here
    }
    printf("\n");
}

int main() {
    
    char password[] = "SecertPAA$sword1234";  // The password we want to steal
    char buffer[50];  // A small buffer
    read_input(buffer, sizeof(buffer));  // Reads up to 50 bytes
    print_buffer(buffer, 100);  // Over-read: prints 100 bytes instead of 50!

    return 0;
}

