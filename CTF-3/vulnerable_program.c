#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Function that prints the flag (our target)
void print_flag() {
printf("🎉 Congratulations! You've exploited the buffer!\n");
printf("flag{buff3r_0v3rfl0w_m4st3r}\n");
exit(0);
}

// Function with intentional buffer overflow vulnerability
void vulnerable_function() {
char buffer[64]; // Small buffer - vulnerable to overflow

printf("Enter your name: ");
fflush(stdout);

// Dangerous function - no bounds checking!
fgets(buffer, 128, stdin);  // This is the vulnerability

printf("Hello, %s!\n", buffer);
printf("Unfortunately, you didn't win this time.\n");
}

int main() {
printf("=== Welcome to the Name Game ===\n");
printf("Tell me your name and maybe you'll get a surprise!\n");
printf("Target function address: %p\n", print_flag); // Give hint

vulnerable_function();

return 0;
}