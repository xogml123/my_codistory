/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/29 23:18:25 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 23:18:29 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdbool.h>

unsigned int	ft_strlen(char *base)
{
	unsigned int	count;

	count = 0;
	while (base[count] != '\0')
		count++;
	return (count);
}

bool	is_base(char *base)
{
	int	i;
	int	j;
	int	size;

	size = ft_strlen(base);
	i = 0;
	if (str == 0 || ft_strlen(base) <= 1)
		return (false);
	while (base[i] != '\0')
	{
		if (base[i] == '+' || base[i] == '-')
			return (false);
		i++;
	}
	i = 0;
	j = 0;
	while (i < size)
	{
		while(j < size)
		{
			if (base[i] == base[j])
				return (false);
			j++;
		}
		i++;
	}
	return (true);
}

void	ft_putnbr_base_write(char *base, int nbr)
{
	int	radix;

	radix = ft_strlen(base);
	if (nbr == -2147483648)
	{
		write(1, "-", 1);
		ft_putnbr_base_write(base, -((-nbr) % radix)-nbr);
		write(1, base + ((-nbr) % radix), 1);

	}
	else if (nbr < 0)
	{
		write(1, "-", 1);
		ft_putnbr_base_write(base, -nbr);
	}
	else
	{
		if (nbr radix >= 10)
		{
			ft_putnbr_base_write(base, nbr / radix);
			write(1, &base[nbr % radix], 1);
		}
		else
			write(1, &base[nbr], 1);
	}
}

void	ft_putnbr_base(int nbr, char *base)
{
	if (is_base(base) == false)
		return ;
	ft_putnbr_base_write(base, nbr);
}
