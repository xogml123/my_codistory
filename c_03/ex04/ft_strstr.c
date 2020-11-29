/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/29 22:16:49 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 22:19:42 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strstr(char *str, char *to_find)
{
	int		i;
	int		j;
	char	*first;

	i = 0;
	j = 0;
	first = NULL;
	while (1)
	{
		if (str[i] == '\0' || to_find[i] == '\0')
			break ;
		if (str[i] == to_find[j])
		{
			if (first == NULL)
				first = &str[i];
			j++;
		}
		i++;
	}
	if (to_find[i] == '\0')
	{
		return (first);
	}
	else
		return (NULL);
}
