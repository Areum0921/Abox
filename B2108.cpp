#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int arr[500001];
int brr[500001];
int compare(const void *first, const void *second);


int main()
{
	int i, j,N,max=0,min=4001,k;
	float sum = 0;
	int cnt = 1, mcnt = 1, p = 0, scnt = 1;

	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		scanf("%d", &arr[i]);
		sum += arr[i];
	}
	int arr_size = sizeof(arr) / sizeof(int);
	qsort(arr, arr_size, sizeof(int), compare);
	
	for(j = 0; j < N; j++) //최다 빈출횟수 구하기.
	{
		if (arr[j] == arr[j + 1])
			cnt += 1;
		if (mcnt < cnt)//중복횟수 제일 큰값
			mcnt = cnt; //mcnt만큼 반복되는 숫자가 제일 많이 나옴.
		else
			cnt = 1;
	}
	for (k = 0; k < N; k++) //범위 구하기용 max값과 min값 
	{
		if (arr[k] > max)
			max = arr[k];

		if (arr[k] < min)
			min = arr[k];
		
	}
	for (int l = 0; l < N; l++)
	{
		
		if (arr[l] == arr[l + 1])
			scnt += 1;
		else
			scnt = 1;

		if (scnt == mcnt)
		{
			brr[p] = arr[l];
			p+=1;
			
		}
		
	}
	printf("%.0f\n", roundf(sum/N)); // 평균 소수첫째자리 반올림
	printf("%d\n", arr[N / 2]);//중앙값 정렬된 행렬의 가운데값 여기서 N은 홀수로 고정
	if (N == 1) 
	{
		printf("%d\n", arr[0]);
		printf("0\n");
	}
	else
	{
		printf("%d\n", brr[1]);
		printf("%d\n", max - min);
	}
	
	
}
int compare(void* first, void* second) {
	if (*(int*)first > *(int*)second) return 1;
	else if (*(int*)first < *(int*)second) return -1;
	else return 0;
}