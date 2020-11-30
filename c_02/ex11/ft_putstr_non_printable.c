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

void	ft_putchar(char ch)
{
	write(1, &ch, 1);
}

void	ft_putstr_non_printable(char *str)
{
	int	flag;
	int i;
	unsigned char	current;

	i = 0;
	while (str[i] != '\0')
	{
		current = str[i];
		flag = ft_is_printable(current);
		if (flag == 0)
		{
			ft_putchar('\\');
			ft_putchar("0123456789abcdef"[current / 16]);
			ft_putchar("0123456789abcdef"[current % 16]);
		}
		else
			write(1, str + i, 1);
		i++;
	}
}
