# 규칙찾기
# dp[1]=1, dp[2]=3, dp[3]=5, dp[4]=11, dp[5]=21
dp=[0,1,3]
N=int(input())
for i in range(3,N+1):
    dp.append(dp[i-1]+(dp[i-2]*2))

print(dp[N]%10007)