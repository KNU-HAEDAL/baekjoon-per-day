#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int arr[9];
	int len = sizeof(arr)/sizeof(int);

	for (int i = 0; i < len; i++)
	{
		scanf(" %d", &arr[i]);
	}
	
	int max = arr[0];
	int index = 0;

	for (int j = 1; j < len; j++) {
		if (max < arr[j])
		{
			max = arr[j];
			index = j;
		}
	}

	printf("%d \n", max);
	printf("%d \n", index + 1);

	return 0;
}