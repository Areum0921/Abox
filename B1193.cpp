#include <stdio.h>

int main()
{
	int a;
	scanf("%d", &a);
	int sum = 0, n = 1;
	while (sum < a)
	{
		sum += n;
		n++;
	}

	int sum2 = sum - n + 1; // �ٷ� �����ϱ� �� �׷��� ��
	int sum3 = a - sum2; // �ڱⰡ ���Ե� �׷쿡���� ����
	if (n % 2 == 1)
	{
		printf("%d/%d", sum3, n - sum3);
	}
	else if (n % 2 == 0)
	{
		printf("%d/%d", n - sum3, sum3);
	}

}