/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_combn.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <takim@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/22 04:40:10 by takim             #+#    #+#             */
/*   Updated: 2020/11/25 21:57:18 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void		ft_print_combn2(char start, int index, int n, char *ch);

void		ft_print_combn(int n)
{
	char	ch[11];

	if (n < 1 || n > 9)
		return ;
	ch[10] = n;
	ft_print_combn2('0', 0, n, ch);
}

void		ft_print_combn2(char start, int index, int n, char *ch)
{
	char	i;

	if (n != 0)
	{
		i = start;
		while (i <= 58 - ch[10] + index)
		{
			ch[index] = i;
			ft_print_combn2(i + 1, index + 1, n - 1, ch);
			i++;
		}
	}
	else
	{
		write(1, ch, index + 1);
		if (ch[0] != (10 - ch[10]) + 48)
			write(1, ", ", 2);
	}
}
