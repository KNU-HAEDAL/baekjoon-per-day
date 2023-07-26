#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int n, v;
	scanf("%d", &n);

	int input[100];
	for (int i = 0; i < n; i++)
		scanf(" %d", &input[i]);
	
	scanf(" %d", &v);

	int num = 0;	// input 배열에 있는 정수 v의 개수
	for (int i = 0; i < n; i++)
	{
		if (v == input[i])
			num++;
	}

	printf("%d", num);
}