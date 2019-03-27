#include<stdio.h>

int main()
{
	int arr[15][15], T;
	int x,y,i, j,k;

	for (i = 0; i < 15; i++)
	{
		arr[i][0] = 1; // 몇층이든 첫번째 1호는 1명
		arr[0][i] = i + 1; // 0층일경우 호수만큼 산다. 0층 6호 = 6명
	}
	for (i = 1; i < 15; i++)
	{
		for (j = 1; j < 15; j++)
		{
			arr[i][j] = arr[i - 1][j] + arr[i][j - 1]; //규칙을 찾아보면 n층 m호 사람수는 n-1층 m호 + n층 m-1호
		}
	}
	scanf("%d", &T);
	for (k = 0; k < T; k++)
	{
		scanf("%d", &x);
		scanf("%d", &y);
		int ans = arr[x][y-1]; //층은 0층부터 호수는 1호부터
		printf("%d\n",ans);
	}

}