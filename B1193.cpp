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

	int sum2 = sum - n + 1; // 바로 포함하기 전 그룹의 합
	int sum3 = a - sum2; // 자기가 포함된 그룹에서의 순서
	if (n % 2 == 1)
	{
		printf("%d/%d", sum3, n - sum3);
	}
	else if (n % 2 == 0)
	{
		printf("%d/%d", n - sum3, sum3);
	}

}