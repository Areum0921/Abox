#include <iostream>
int blist[1000001];
long long profit;
using namespace std;
int main()
{
	int T;
	cin >> T;
	for (int k = 0; k < T; k++) { //�׽�Ʈ ���̽��� ��ŭ ����
		int N, max;
		profit = 0; //�׽�Ʈ ���̽� ���۽� ���� profit �ʱ�ȭ
		cin >> N; // ���� ���� �Ⱓ�Է�

		for (int i = 0; i < N; i++) // ���� �Է�
		{
			scanf("%d", &blist[i]);
		}
		max = blist[N - 1]; //�� ���������� max������ 
		for (int j = N - 2; j >= 0; j--)
		{
			if (max < blist[j])
			{
				max = blist[j];
			}
			else
			{
				profit = profit + (max - blist[j]);
			}
		}

		printf("#%d %ld\n", k + 1, profit);

	}
}