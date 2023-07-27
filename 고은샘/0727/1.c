#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int attend[30] = { 0 };
	int length = sizeof(attend) / sizeof(int);
	int a;	// 인덱스 저장할 변수

	for (int i = 0; i < length - 2; i++) // 과제 제출한 학생 입력
	{
		scanf("%d", &a);
		attend[a - 1] = 1;
	}

	for (int j = 0; j <= length; j++)
	{
		if (attend[j] == 0)
			printf("%d\n", j + 1);
	}

	return 0;
}