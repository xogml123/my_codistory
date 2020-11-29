/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <takim@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/25 00:54:39 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 20:49:40 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

unsigned	int	ft_strlen(char *str)
{
	int				i;
	unsigned	int	count;

	i = 0;
	count = 0;
	while (1)
	{
		if (str[i] == '\0')
			break ;
		count++;
		i++;
	}
	return (count);
}

unsigned	int	ft_strlcpy(char *dest, char *src, unsigned int size)
{
	unsigned int	i;
	unsigned int	min;

	i = 0;
	if (size == 0)
		return (ft_strlen(src));
	if (ft_strlen(src) == 0)
		return (0);
	min = (ft_strlen(src) >= size) ? size : ft_strlen(src);
	while (i < min - 1)
	{
		dest[i] = src[i];
		i++;
	}
	while (i < size)
	{
		dest[i] = '\0';
		i++;
	}
	return (ft_strlen(src));
}
