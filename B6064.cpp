#include<stdio.h>
int gcd(int a, int b)
{
	int temp;
	while (b != 0)
	{
		temp = a%b;
		a = b;
		b = temp;
	}
	return a;
}
int lcm(int c, int d)
{
	int gvalue;
	gvalue = gcd(c, d);
	if (gvalue == 0)
	{
		return 0; // 인수가 둘다 0일때 
	}
	return c*d / gvalue;
}

int main()
{
	int T, M, N, x, y,cnt;
	
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		
		scanf("%d %d %d %d", &M, &N, &x, &y);
		int q;
		while (1)
		{
			if (x > lcm(M, N))
			{
				cnt = -1;
				break;
			}
			q = x%N;
			if (q == 0)
			{
				q = N;
			}
			if (q == y)
			{
				cnt = x;
				break;
			}
			

			
			x = x + M;

		}

		printf("%d\n", cnt);
	}
}