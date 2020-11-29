/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_params.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/29 23:29:04 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 23:29:24 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	putstr(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		write(1, str + i, 1);
		i++;
	}
}

int		main(int argc, char *argv[])
{
	int	i;

	i = argc - 1;
	while (i > 0)
	{
		putstr(argv[i]);
		write(1, "\n", 1);
		i--;
	}
	return (0);
}
