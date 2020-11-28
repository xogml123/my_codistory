#include <stdio.h>

int main(void) {
	int num = 10;
	int* ptr1 = &num;
	int* ptr2 = ptr1;
	char* str1 = "hello1";
	char str2[] = "hello2";
	(*ptr1)++;
	(*ptr2)++;
	printf("%d \n", num);
	

	return 0;
}