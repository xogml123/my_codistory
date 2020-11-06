#include <stdio.h>
#include <string.h>
int main() {
	char str[10];
	strcpy_s(str,10, "hello");
	printf("%s", str);
	return 0;
}