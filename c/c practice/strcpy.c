#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int	ft_atoi(const char* str) {
	int i = 0;
	int null_index = 0;
	int num = 0;

		while (str[i] != '\0') {
			i++;

	}
		null_index = i;
		
		for (int j = null_index-1; j >=0 ; j--) {
			num += pow(10.0,(double)(null_index-1-j)) * (str[j]-48);

	}
		return num;
}

int main() {
	char* a = "1234";
	int result = 0;
	result = ft_atoi(a);
	printf("%d", result);
	
	return 0;
}