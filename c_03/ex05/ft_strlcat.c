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
	int dest_len;

	dest_len = ft_strlen(dest);
	i = 0;
	j = ft_strlen(dest);
	while ((src[i] != '\0') && i < (int)(size - dest_len - 1))
	{
		dest[j] = src[i];
		i++;
		j++;
	}
	dest[j] = '\0';
	if (size >= ft_strlen(dest) + ft_strlen(src) + 1)
		return (ft_strlen(dest) + ft_strlen(src));
	else if (size <= ft_strlen(dest))
		return (ft_strlen(dest));
	else
		return (j);
}
