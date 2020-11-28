
int	ft_recursive_factorial(int nb)
{
	if (nb == 0)
		return (1);
	else if (nb >= 0)
	{
		return (nb * ft_recursive(nb - 1));
	}
	else
		return (0);
}
