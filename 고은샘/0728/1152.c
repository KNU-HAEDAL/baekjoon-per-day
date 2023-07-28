#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	char arr[1000001];
	int j = 0, w = 0;

	scanf("%[^\n]s", &arr);

	while (arr[j] == ' ')
	{
		j++;
	}

	while (arr[j])
	{
		if (arr[j] == ' ')
			w++;
		j++;
	}

	if (arr[j - 1] == ' ')
		w--;

	printf("%d", w + 1);

	return 0;
}