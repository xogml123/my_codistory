/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_non_printable.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/25 22:58:13 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 21:01:17 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int		ft_is_printable(char ch)
{
	if (ch >= 32 && ch <= 126)
		return (1);
	else
		return (0);
}

char	ft_hexa(char ch)
{
	if (ch >= 0 && ch <= 9)
		return (ch + 48);
	else
		return (ch + 87);
}

void	ft_unprintable_print(char ch)
{
	int		target;
	char	q;
	char	r;

	target = (int)ch;
	write(1, "\\", 2);
	q = ch / 16;
	r = ch % 16;
	q = ft_hexa(q);
	r = ft_hexa(r);
	write(1, &q, 1);
	write(1, &r, 1);
}

void	ft_putstr_non_printable(char *str)
{
	int	flag;
	int i;

	i = 0;
	while (str[i] != '\0')
	{
		flag = ft_is_printable(str[i]);
		if (flag == 0)
			ft_unprintable_print(str[i]);
		else
			write(1, str + i, 1);
		i++;
	}
}
