# 이것도 프로그래머스 3레벨인게 이상하다.
# n=1 1 / n=2 2 / n=3 3 / n=4 5 / n=5 8
# dp[n] = dp[n-1]+dp[n-2]


def solution(n):
    answer = 0
    dp=[0]*(n+1)
    dp[1]=1
    if(n>1):
        dp[2]=2
    for i in range(n+1):
        dp[i]=(dp[i-1]+dp[i-2])%1000000007
    return answer