/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_memory.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/25 23:37:04 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 21:06:12 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_hexa_print(unsigned long num, int size)
{
	char	str[size];
	int		i;

	i = size - 1;
	while (i >= 0)
	{
		str[i] = num % 16;
		num -= str[i];
		num /= 16;
		i--;
	}
	i = size - 1;
	while (i >= 0)
	{
		if (str[i] <= 9)
			str[i] += 48;
		else if (str[i] <= 15)
			str[i] += 87;
		i--;
	}
	write(1, str, size);
}

void	ft_print_char(char *temp_addr, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if (temp_addr[i] >= 32 && temp_addr[i] <= 126)
			write(1, temp_addr + i, 1);
		else
			write(1, ".", 1);
		i++;
	}
}

void	ft_print_oneline(char *temp_addr, int size)
{
	int	i;

	if (size >= 16)
		size = 16;
	ft_hexa_print((unsigned long)temp_addr, 16);
	write(1, ": ", 2);
	i = 0;
	while (i < size)
	{
		if (i % 2 == 0)
			ft_hexa_print((unsigned long)*(temp_addr + i), 2);
		else
		{
			ft_hexa_print((unsigned int)*(temp_addr + i), 2);
			write(1, " ", 1);
		}
		i++;
	}
	write(1, "    ", 4);
	ft_print_char(temp_addr, size);
	write(1, "\n", 1);
}

void	*ft_print_memory(void *addr, unsigned int size)
{
	char	*temp_addr;
	int		i;

	temp_addr = (char *)addr;
	i = 0;
	while (temp_addr < (char *)addr + size)
	{
		ft_print_oneline(temp_addr, size - 16 * i);
		temp_addr += 16;
		i++;
	}
	return ((void *)addr);
}
