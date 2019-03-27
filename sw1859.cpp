#include <iostream>
int blist[1000001];
long long profit;
using namespace std;
int main()
{
	int T;
	cin >> T;
	for (int k = 0; k < T; k++) { //테스트 케이스수 만큼 실행
		int N, max;
		profit = 0; //테스트 케이스 시작시 이익 profit 초기화
		cin >> N; // 가격 예측 기간입력

		for (int i = 0; i < N; i++) // 가격 입력
		{
			scanf("%d", &blist[i]);
		}
		max = blist[N - 1]; //맨 마지막날을 max값으로 
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