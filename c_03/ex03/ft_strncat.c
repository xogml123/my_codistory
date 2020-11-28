
char	*ft_strncat(char *dest, char *src, unsigned int nb)
{
	int	i;

	i = 0;
	while (dest[i] != '\0')
		i++;
	while (*src != '\0' && nb > 0)
	{
		dest[i] = *src;
		i++;
		nb--;
		src++;
	}
	*dst = '\0';
	return (dest);
}
