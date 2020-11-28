#include <stdio.h>
int add() {
	static int x;
	int y = 1;
	printf("%d %d", x, y);
}
void main() {
	int x = 5;
	add();


}