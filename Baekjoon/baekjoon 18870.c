#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
int main()
{
	int	a;
	int	*arr;
	int	temp;
	int	*result;
	char ch;

	scanf("%d\n", &a);
	arr = malloc(sizeof(int) * a);
	result = malloc(sizeof(int) * a);
	bzero(result, a);
	for (int i = 0; i < a; i++)
	{
		scanf("%d", &temp);
		scanf("%c", &ch);
		arr[i] = temp;
	}
	for (int i = 0; i < a; i++)
	{
		for (int j = 0; j < a; j++)
		{
			if (arr[i] > arr[j])
				result[i]++;
		}
	}

	for (int i = 0; i < a; i++)
	{
		printf("%d\t", result[i]);
	}
	free(arr);
	free(result);
	return (0);
}