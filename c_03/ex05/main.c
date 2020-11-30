#include <stdio.h>
extern unsigned int	ft_strlcat(char *dest,char *src, unsigned int size);
int	main(int argc, char **argv)
{
	char *s1 = argv[1];
	char *s2 = argv[2];
	argc = 3;
	printf("%d",argc);
	printf("%d",ft_strlcat(s1,s2,2));
	printf("%s",s1);
	return (0);
}

