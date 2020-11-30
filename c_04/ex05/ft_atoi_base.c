/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/29 23:18:38 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 23:23:57 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdbool.h>

int				is_type(char c, char *base)
{
	if (ft_base_int(c, base) >= 0)
		return (1);
	else if (c == '-')
		return (-1);
	else if (c == ' ' || c == '\n' || c == '\t' || c == '\r'
			|| c == '\v' || c == '\f')
		return (0);
	else
		return (2);
}

bool			is_base(char *base)
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
	i = -1;
	j = -1;
	while (++i < size)
	{
		while (++j < size)
		{
			if (base[i] == base[j])
				return (false);
		}
	}
	return (true);
}

unsigned int	ft_strlen(char *base)
{
	unsigned int	count;

	count = 0;
	while (base[count] != '\0')
		count++;
	return (count);
}

int				ft_base_int(char ch, char *base)
{
	int				index;
	unsigned int	size;

	index = 0;
	size = ft_strlen(base);
	while (index < size)
	{
		if (ch == base[index])
			return (index);
		index++;
	}
	return (-1);
}

int				ft_atoi_base(char *str, char *base)
{
	int	result;
	int	sign;
	int	i;
	int	radix;

	if (is_base(base) == false)
		return ;
	result = 0;
	sign = 1;
	i = 0;
	radix = ft_strlen(base);
	while (is_type(str[i], base) == 0)
		i++;
	while (is_type(str[i], base) == -1)
	{
		sign *= -1;
		i++;
	}
	while (is_type(str[i], base) == 1)
	{
		result *= radix;
		result += ft_base_int(str[i], base);
		i++;
	}
	return (result * minus);
}
