#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define STUDENT 30

int main(void)
{
    int std[STUDENT], i, j, cnt = 28, temp;

    for (i = 0; i < STUDENT; i++) // 초기화 
        std[i] = STUDENT + 1;

    for (i = 0; i < 28; i++)
        scanf("%d", &std[i]);

    for (i = 0; i < STUDENT; i++)
    {
        if (std[i] != (i + 1))
        {
            for (j = 0; j < STUDENT; j++)
            {
                if (std[j] == (i + 1))
                {
                    temp = std[i];
                    std[i] = std[j];
                    std[j] = temp;
                    break;
                }
                else if (j == (STUDENT - 1))
                {
                    temp = std[i];
                    std[i] = std[cnt];
                    std[cnt++] = temp;
                }
            }
        }
    }

    for (i = 0; i < STUDENT; i++)
    {
        if (std[i] == 31)
            printf("%d\n", i + 1);
    }

    return 0;
}