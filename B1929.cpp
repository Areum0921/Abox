//�ش���� ������ �Ҽ���� ���������� ������ �Ҽ��� 2,3,5,7,11,13 ....

#include<stdio.h>
int arr[1000001];

int main()
{

	int M, N, i, j,k;

	scanf("%d %d", &M, &N);

	for (i = M; i <= N; i++)
	{
		arr[i - M] = i; //�迭�ȿ� ������ ���ڵ��� �־��ֱ�
	}

	for (j = 0; j <= N - M; j++)
	{
			
	}
}
