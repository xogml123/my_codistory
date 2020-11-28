
#include <stdio.h>
int main(void)
{
	char* str = "hello";
	str = (unsigned int)(str);
	printf("%x", str);
	return 0;
}