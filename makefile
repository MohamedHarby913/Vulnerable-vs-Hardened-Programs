# Compiler
CC = gcc

# Compiler Flags for the vulnerable program (disables protections)
CFLAGS = -fno-stack-protector -z execstack -g  

# Default target: Compile both programs
all: VulnerableProgram SecureProgram

# Compile the vulnerable program
vulnerable_program:
	$(CC) $(CFLAGS) VulnerableProgram.c -o VulnerableProgram

# Compile the secure program
secure_program:
	$(CC) SecureProgram.c -o SecureProgram

# Clean up compiled files
clean:
	rm -f VulnerableProgram SecureProgram VulnerableOutput.txt SecureOutput.txt

