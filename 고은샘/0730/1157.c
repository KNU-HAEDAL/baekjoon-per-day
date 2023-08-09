#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void)
{
   char arr[1000005];
   int ascii[26] = { 0, };
   int len, max = 0;
   char answer;

   scanf("%s", arr);
   len = strlen(arr);

   for (int i = 0; i < len; i++)
   {
      if (arr[i] >= 'a')
         ascii[arr[i] - 'a']++;
      else
         ascii[arr[i] - 'A']++;
   }

   for (int i = 0; i < 26; i++)
   {
      if (ascii[i] == max)
      {
         answer = '?';
      }
      else if (ascii[i] > max)
      {
         max = ascii[i];
         answer = 'A' + i;
      }
   }

   printf("%c", answer);

   return 0;
}