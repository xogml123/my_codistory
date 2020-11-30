/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/29 21:59:14 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 21:59:20 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strncat(char *dest, char *src, unsigned int nb)
{
	int	i;

	i = 0;
	while (dest[i] != '\0')
		i++;
	while (*src != '\0' && nb > 0)
	{
		dest[i] = *(unsigned char *)src;
		i++;
		nb--;
		src++;
	}
	*dst = '\0';
	return (dest);
}
