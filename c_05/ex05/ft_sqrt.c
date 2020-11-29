/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/29 23:26:34 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 23:26:52 by takim            ###   ########.fr       */
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
			return (0);
		else if (temp == (unsigned int)nb)
			return (i);
		else
			continue;
		i++;
	}
}
