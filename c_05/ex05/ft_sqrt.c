
int	ft_sqrt(int nb)
{
	int	i;
	unsigned int	temp;

	i = 0;
	while (1)
	{
		temp = (unsigned int)(i * i);
		if (temp > (unsigned int)nb)
			return (0);
		else if (temp == (unsigned int)nb)
			return (i);
		else
			continue;
		i++;
	}
}
