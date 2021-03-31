N,K = map(int,input().split(" "))
dp=[[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1): # 0~i까지 1개 골라서 i가 되는 경우는 1가지
    dp[i][1]=1

for k in range(K+1): # 0~1까지 k개 골라서 1이 되는 경우는 1한개와 0으로 이루어지는 경우들 --> k개
    dp[1][k]=k

for l in range(2,N+1):
    for m in range(2,K+1):
        dp[l][m]=dp[l-1][m]+dp[l][m-1]
# 규칙
# dp[2][2] = 3  dp[2][3] = 6    --> dp[a][b] = dp[a-1][b]+dp[a][b-1]
# dp[3][2] = 4  dp[3][3] = 10
# dp[4][2] = 5  dp[4][3] = 15
# dp[5][2] = 6  dp[5][3] = 21
print(dp[N][K]%1000000000)