/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_prime.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/29 23:27:07 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 23:27:29 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_sqrt(int nb)
{
	int				i;
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
	if (nb >= 2 && nb <= 3)
		return (1);
	i = 2;
	while (i < ft_sqrt(nb) + 1)
	{
		if (nb % i == 0)
			return (0);
		i++;
	}
	return (1);
}
