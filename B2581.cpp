#include<stdio.h>

int main()
{

	int M,N,i, j, sum=0,x=0,cnt,check=0;
	int min[10001];
	scanf("%d\n %d", &M,&N);
	
	for (i = M; i <= N; i++)
	{
		cnt = 0;
		for (j = 1; j<i; j++)
		{
			if (i%j == 0)
			{
				cnt += 1;
			}
		}

		if (cnt == 1)//i가 소수 일때
		{
			sum = sum + i;//소수값 더해가기
			min[x] = i;
			x += 1;
			check += 1; //소수 개수 
		}
	}

	if (check == 0)
		printf("%d",check-1);//소수가 0개일때 -1출력
	else {
		printf("%d\n", sum);//두 수 사이의 소수들의 합
		printf("%d\n", min[0]); //맨처음오는 소수값
	}
}
