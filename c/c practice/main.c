extern char **ft_split(char *str);
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
	/*
	char *str;
	char **result;
	
	str = "   hello, world  ";
	result = ft_split(str);

	printf("%s", result[0]);
	printf("%s", result[1]);
	*/
	int *str =(int*)malloc(sizeof(int)*2);
	str[1]=1;
	str[0]=0;

	printf("%d%d",str[0],str[1]);

}
