
#include <unistd.h>

void	putstr(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		write(1, str+i, 1);
		i++;
	}
}

int	main(int argc, char *argv[])
{
	int	i;

	i = argc - 1;
	while (i > 0)
	{
		putstr(argv[i]);
		write(1, "\n", 1);
		i--;
	}
	return (0);
}
