#include <stdio.h>
#include <stdlib.h>

int main() {
	int* a = (int*)malloc(sizeof(int)*3);

	*a =0;
	*(a+1) =1;
	*(a+2) =2;
	printf("%d%d%d", a[0], a[1], a[2]);
}
