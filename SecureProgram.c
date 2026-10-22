#include <stdio.h>
#include <string.h>

// this function is to read the input buffer
void read_input(char *buffer, int size) {
    printf("Enter your username to access your account\n");
    fgets(buffer, size, stdin);
}

// this function is to print the output buffer
void print_buffer(char *buffer, int size) {
    printf("Buffer Content: ");
    for (int i = 0; i < size; i++) {
        printf("%c", buffer[i]);
    }
    printf("\n");
}

int main() {
    char password[] = "SecertPAA$sword1234";  // The password we want to steal
    char buffer[50];
  
    // reading and printing the same size of buffer, preventing buffer over-read
    read_input(buffer, sizeof(buffer)); 
    print_buffer(buffer, sizeof(buffer));

    return 0;
}

