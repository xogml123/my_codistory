
#include <unistd.h>

void	ft_write_deligate(char ch)
{
	write(1, &ch, 1);
}

void	ft_putnbr(int nb)
{
	if (nb == -2147483648)
	{
		write(1, "8", 1);
		ft_putnbr(nb / 10);
	}
	else if (nb < 0)
	{
		write(1, "-", 1);
		ft_putnbr(-nb);
	}
	else
	{
		if (nb > 9)
			ft_putnbr(nb / 10);
		else
			ft_write_deligate((nb % 10) + 48);
	}
}
