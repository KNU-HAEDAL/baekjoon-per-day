#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int hour, min;
	int outputH, outputM;

	scanf("%d %d", &hour, &min);
	if ((min - 45) >= 0 ) {
		outputH = hour;
		outputM = min - 45;
	}
	else {
		if (hour == 0)
			hour = 24;
		outputH = hour - 1;
		outputM = (60 + min) - 45;
	}

	printf("%d %d", outputH, outputM);
}