/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: takim <takim@student.42seoul.kr>           +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/11/25 00:25:46 by takim             #+#    #+#             */
/*   Updated: 2020/11/29 20:24:11 by takim            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_type(char ch)
{
	if (ch >= '0' && ch <= '9')
		return (0);
	else if (ch >= 'A' && ch <= 'Z')
		return (1);
	else if (ch >= 'a' && ch <= 'z')
		return (2);
	else
		return (3);
}

char	*ft_strcapitalize(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (i == 0)
		{
			if (ft_type(str[i]) == 2)
				str[i] -= 32;
		}
		else if ( i > 0)
		{
			if (ft_type(str[i]) == 2 && ft_type(str[i - 1]) == 3)
				str[i] -= 32;
			else if (ft_type(str[i]) == 1 && ft_type(str[i - 1] != 3))
				str[i] += 32;
		}
		i++;
	}
	return (str);
}
