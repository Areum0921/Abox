//해당숫자 이하의 소수들로 나누어지지 않을때 소수임 2,3,5,7,11,13 ....

#include<stdio.h>
int arr[1000001];

int main()
{

	int M, N, i, j,k;

	scanf("%d %d", &M, &N);

	for (i = M; i <= N; i++)
	{
		arr[i - M] = i; //배열안에 범위의 숫자들을 넣어주기
	}

	for (j = 0; j <= N - M; j++)
	{
			
	}
}
