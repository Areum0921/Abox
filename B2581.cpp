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

		if (cnt == 1)//i�� �Ҽ� �϶�
		{
			sum = sum + i;//�Ҽ��� ���ذ���
			min[x] = i;
			x += 1;
			check += 1; //�Ҽ� ���� 
		}
	}

	if (check == 0)
		printf("%d",check-1);//�Ҽ��� 0���϶� -1���
	else {
		printf("%d\n", sum);//�� �� ������ �Ҽ����� ��
		printf("%d\n", min[0]); //��ó������ �Ҽ���
	}
}
