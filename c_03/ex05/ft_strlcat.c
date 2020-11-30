/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/29 22:20:42 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 23:11:58 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

unsigned int	ft_strlen(char *str)
{
	unsigned int	count;

	count = 0;
	while (str[count] != '\0')
		count++;
	return (count);
}

unsigned int	ft_strlcat(char *dest, char *src, unsigned int size)
{
	int	i;
	int	j;
	unsigned int dest_size;
	unsigned int src_size;

	i = 0;
	j = ft_strlen(dest);
	dest_size = ft_strlen(dest);
	src_size = ft_strlen(src);
	while ((src[i] != '\0') && i < (int)(size - dest_size - 1))
	{
		dest[j] = src[i];
		i++;
		j++;
	}
	dest[j] = '\0';
	if (size >= ft_strlen(dest) + ft_strlen(src) + 1)
		return (dest_size + src_size);
	else if (size <= ft_strlen(dest))
		return (dest_size);
	else
		return (j);
}
