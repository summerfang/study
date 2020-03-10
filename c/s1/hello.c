#include <stdio.h>

int add(int x, int y);

int main()
{
	int c = add(2,2);
	printf("%d",c);
	printf("Hello, World!");
}

int add(int x, int y)
{
	return x + y;
}
