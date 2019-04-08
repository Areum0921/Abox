#include<stdio.h>

int main()
{
	int N;
	int i = 1, j = 6;
	int T = 1;

	scanf("%d", &N);

	while (N > i)
	{
		if (N == 1) {
			break;
		}
		else {
			T++;
			i = i + j;
			if (i < N) {
				j += 6;
			}
		}

	}
	printf("%d", T);
}