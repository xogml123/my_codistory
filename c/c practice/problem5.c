#include <stdlib.h>
#include <stdio.h>
int	ft_is_space(char ch);
int	*ft_lengths(char *str);
int	ft_wordcount(char *str);
int	ft_is_space(char ch);
void	ft_split_deligate(char* str,char **words);

int	ft_is_space(char ch)
{
	if (ch == '\n' || ch == '\t' || ch == ' ')
		return (1);
	else
		return (0);
}

int	*ft_lengths(char* str)
{
	int	count;
	int	index;
	int	*lengths;
	int	flag;
	int	i;

	lengths = (int*)malloc(2 * sizeof(int));
	count = 0;
	flag = 1;
	index = 0 ;
	i = 0;
	while (str[i] != '\0')
	{
		if (ft_is_space(str[i]) == 0)
		{
			flag = 0;
			count++;
		}
		else if (ft_is_space(str[i]) == 1 && flag == 0)
		{
			lengths[index++] = ++count;
			flag = 1;
			count = 0 ;
		}
		i++;
	}
	if (str[i] == '\0' && flag == 0)
		lengths[index] = ++count;
	return (lengths);
}

int	ft_wordcount(char *str)
{
	int count;
	int	i;
	int	flag;

	flag = 1;
	i = 0 ;
	count = 0;
	while (str[i] != '\0')
	{
		if (ft_is_space(str[i]) == 0 && flag == 1)
		{
			count++;
			flag = 0;
		}
		else if (ft_is_space(str[i]) == 1)
			flag = 1;
		i++;
	}
	return (count);
}

void	ft_split_deligate(char* str,char **words)
{
	int	index;
	int	flag;

	flag = 1;
	index = 0;
	while (*str != '\0')
	{
		if (ft_is_space(*str) == 0)
		{
			(*words[index]) = *str;
			(words[index])++;
			flag = 0;
		}
		else if (ft_is_space(*str) == 1 && flag == 0)
		{
			flag = 1;
			*(words[index++]) = '\0';
		}
		str++;
	}
	if (flag == 0)
		*(words[index]) = '\0';
}
char	**ft_split(char* str)
{
	char	**words;
	int	index;
	int	*lengths;
	words = malloc(2* sizeof(char*));
	lengths = ft_lengths(str);

	index = 0;
	while (index < ft_wordcount(str))
	{
		words[index] = (char*)malloc(sizeof(char) * (lengths[index]+1));
		index++;
	}
	ft_split_deligate(str, words);
	index = 0;
	while (index < ft_wordcount(str))
	{
		words[index] -= lengths[index] - 1;
		index++;
	}
	return (words);
}

int main(void)
{
	char str[15] = "hello al";
	char** result = ft_split(str);

	printf("%s\n", result[0]);
	printf("%s\n", result[1]);
	return (0);
}
