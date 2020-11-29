/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/29 13:07:47 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 13:29:00 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_write_deligate(char ch)
{
	write(1, &ch, 1);
}

void	ft_putnbr(int nb)
{
	if (nb == -2147483648)
	{
		ft_putnbr(nb / 10);
		write(1, "8", 1);
	}
	else if (nb < 0)
	{
		write(1, "-", 1);
		ft_putnbr(-nb);
	}
	else if (nb >= 0)
	{
		if (nb > 9)
		{
			ft_putnbr(nb / 10);
			ft_write_deligate((nb % 10) + 48);
		}
		else
			ft_write_deligate((nb % 10) + 48);
	}
}
