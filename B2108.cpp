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
	
	for(j = 0; j < N; j++) //�ִ� ����Ƚ�� ���ϱ�.
	{
		if (arr[j] == arr[j + 1])
			cnt += 1;
		if (mcnt < cnt)//�ߺ�Ƚ�� ���� ū��
			mcnt = cnt; //mcnt��ŭ �ݺ��Ǵ� ���ڰ� ���� ���� ����.
		else
			cnt = 1;
	}
	for (k = 0; k < N; k++) //���� ���ϱ�� max���� min�� 
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
	printf("%.0f\n", roundf(sum/N)); // ��� �Ҽ�ù°�ڸ� �ݿø�
	printf("%d\n", arr[N / 2]);//�߾Ӱ� ���ĵ� ����� ����� ���⼭ N�� Ȧ���� ����
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