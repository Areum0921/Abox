#include<stdio.h>

int main()
{
	int arr[15][15], T;
	int x,y,i, j,k;

	for (i = 0; i < 15; i++)
	{
		arr[i][0] = 1; // �����̵� ù��° 1ȣ�� 1��
		arr[0][i] = i + 1; // 0���ϰ�� ȣ����ŭ ���. 0�� 6ȣ = 6��
	}
	for (i = 1; i < 15; i++)
	{
		for (j = 1; j < 15; j++)
		{
			arr[i][j] = arr[i - 1][j] + arr[i][j - 1]; //��Ģ�� ã�ƺ��� n�� mȣ ������� n-1�� mȣ + n�� m-1ȣ
		}
	}
	scanf("%d", &T);
	for (k = 0; k < T; k++)
	{
		scanf("%d", &x);
		scanf("%d", &y);
		int ans = arr[x][y-1]; //���� 0������ ȣ���� 1ȣ����
		printf("%d\n",ans);
	}

}