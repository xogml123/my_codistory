/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <takim@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/22 02:28:01 by takim             #+#    #+#             */
/*   Updated: 2020/11/23 22:02:07 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void				ft_comb(char (*ch)[3]);

void				ft_print_comb2(void)
{
	char			ch[105][3];
	char			i;
	char			j;
	int				k;

	k = 0;
	i = '0';
	while (i < 58)
	{
		j = '0';
		while (j < 58)
		{
			ch[k][0] = i;
			ch[k][1] = j;
			k++;
			j++;
		}
		i++;
	}
	ft_comb(&ch[0]);
}

void				ft_comb(char (*ch)[3])
{
	int				i;
	int				j;

	i = 0;
	while (i < 99)
	{
		j = i + 1;
		while (j < 100 && j > i)
		{
			write(1, &ch[i], 2);
			write(1, " ", 1);
			write(1, &ch[j], 2);
			if (i != 98 || j != 99)
			{
				write(1, ", ", 2);
			}
			j++;
		}
		i++;
	}
}
