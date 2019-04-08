#include<stdio.h>

int main()
{
	int a, T, i, j, k, w, temp;
	int arr[1001];
	scanf("%d", &T);

	for (i = 0; i < T; i++)
	{
		scanf("%d", &arr[i]);
	}

	for (int k = 0; k < T; k++)
	{
		for (int w = k; w < T; w++)
		{
			if (arr[k] > arr[w]) {
				temp = arr[k];
				arr[k] = arr[w];
				arr[w] = temp;
			}
		}
	}


	for (j = 0; j < T; j++)
	{
		printf("%d\n", arr[j]);
	}
}