# 처음집을 칠하는 색에따라 3가지 경우
N=int(input())
rgb=[list(map(int,input().split(" "))) for _ in range(N)]
dp=[[0]*3 for _ in range(N)]
dp[0][0]=rgb[0][0] # 0번째집을 빨강,초록,파랑으로 칠할때
dp[0][1]=rgb[0][1]
dp[0][2]=rgb[0][2]

for i in range(1,N):
    #print(dp[i-1][0],dp[i-1][1],dp[i-1][2])
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+rgb[i][0]
    # i번째 집을 빨강으로 칠할때 이전 집의 칠해진 색 초록, 파랑중에 싼거
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+rgb[i][1] # i번째 집을 초록
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+rgb[i][2] # 파랑

print(min(dp[N-1][0],dp[N-1][1],dp[N-1][2]))


