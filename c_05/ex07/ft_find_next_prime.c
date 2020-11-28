
int	ft_sqrt(int nb)
{
	int	i;
	unsigned int	temp;

	i = 0;
	while (1)
	{
		temp = (unsigned int)(i * i);
		if (temp > (unsigned int)nb)
			return (i);
		else if (temp == (unsigned int)nb)
			return (i);
		else
			continue;
		i++;
	}
}

int	ft_is_prime(int nb)
{
	int	i;

	if (nb <= 1)
		return (0);
	if (nb >=2 && nb <= 3)
		return (1);
	i = 2;
	while (i < ft_sqrt(nb) + 3)
	{
		if (nb % i == 0)
			return (0);
		i++;
	}
	return (1);
}

int	ft_find_next_prime(int nb)
{
	while(1)
	{
		if (ft_is_prime(nb) == 1)
			return (nb);
		i++;
	}
}
