
def solution(M,money):
    dp=[999999]*10001
    for i in money: # 해당 금액은 화폐 1개 필요
        dp[i]=1

    for i in range(M+1):
        if dp[i]==999999:
            for j in money:
                if dp[i]>dp[j]+dp[i-j]: # i원을 만들 수 있는 조합중 작은 개수를 사용하는 조합 찾기.
                    dp[i]=dp[j]+dp[i-j]

    if dp[M]==999999: # 999999면 초기값 그대로기 때문에 해당 금액을 만들 수 없음.
        print(-1)
    else:
        print(dp[M])


M=700
money=[3,5,7]
solution(M,money)