#include <stdio.h>

void main() {
	int i;
	float num = 0.0;
	for (i = 0; i < 100; i++) {
		num += 0.1;
	}
	printf("%f", num);
	/*float 은 6자리까지
	  double 은 15 자리까지 정확도가 보장됨*/

	
}