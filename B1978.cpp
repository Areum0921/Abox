#include<stdio.h>

int main()
{
	
	int N, num, i, j,cnt,check=0;

	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		cnt = 0;
		scanf("%d", &num);
		for (j = 1; j <num; j++)
		{
			if (num%j == 0)
			{
				cnt += 1;
			}
		}
		
		if (cnt == 1)
		{
			check=check+1;
		}
	}

	printf("%d\n", check);
	
	
}