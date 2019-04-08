#include<stdio.h>

int main() {
	int N, K;// 학생수, 콘센트수
	int i = 0, j = 0;
	int A[101];
	scanf("%d %d", &N, &K);

	for (j = 0; j < K; j++) {
		scanf("%d", &A[j]);
	}

	int cnt = 0;
	for (i = 0; i < K; i++)
	{
		if (A[i] % 2 == 0)
		{
			cnt += A[i] / 2;
		}
		else
			cnt += (A[i] / 2) + 1;
	}

	if (cnt >= N)
		printf("YES");
	else
		printf("NO");
}
