
unsigned int	ft_strlen(char *str)
{
	unsigned int	count;

	count = 0;
	while (str[i] != '\0')
		count++;
	return (count);
}

unsigned int	ft_strlcat(char *dest, char *src, unsigned int size)
{
	int	i;
	int	j;

	i = 0;
	j = ft_strlen(dest);
	while((src[i] != '\0') && i < (int)(size - dest_len -1))
	{
		dest[j] = src[i];
		i++;
		j++;
	}
	dest[j] = '\0';
	if (size >= ft_strlen(dest) + ft_strlen(src) + 1)
		return (size - 1);
	else if (size <= ft_strlen(dest))
		return (ft_strlen(dest));
	else
		return (j);
}
