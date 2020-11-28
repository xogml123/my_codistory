
int	ft_iterative_factorial(int nb)
{
	int	result;
	int	i;

	if (nb < 0)
		return (0);
	i = 1;
	result = 1;
	while (i < nb + 1)
	{
		result *= i;
		i++;
	}
	return (result);
}
