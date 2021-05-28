# N=1 1
# N=2 3
# N=3 5
# N=4 11
# N=5 21
# dp[N] = dp[N-1]+dp[N-2]*2
# 타일의 종류는 3가지 : 1*2, 2*1, 2*2
def solution(N):
    dp=[0]*1001
    dp[1]=1
    dp[2]=3

    for i in range(3,N+1):
        dp[i]=(dp[i-1]+(dp[i-2]*2))%796796

    print(dp[N])
    return dp[N]

solution(4)