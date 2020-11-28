#include <stdbool.h>

int	is_type(char c)
{
	if (c >= '0' && c <= '9')
		return (1);
	else if (c == '-')
		return (-1);
	else if (c == ' ' || c == '\n' || c == '\t' || c == '\r' 
			|| c == '\v' || c == '\f')
		return (0);
	else
		return (2);
}

int	ft_atoi(char *str)
{
	int	result;
	int	sign;
	int	i;

	result = 0;
	sign = 1;
	i = 0;
	while (is_type(str[i]) == 0)
		i++;
	while (is_type(str[i]) == -1)
	{
		sign *= -1;
		i++;
	}
	while (is_type(str[i]) == 1)
	{
		result *= 10;
		result += str[i] - 48;
		i++;
	}
	return (result * minus);
}
