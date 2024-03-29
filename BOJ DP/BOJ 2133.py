# N이 홀수면 총 칸이 홀수라, 짝수타일들로는 채울 수 없다.
# N=2일땐 그리면 된다. 3
# N=4일땐 N이 2인경우를 이용해 2번 채우고, N=4일때만 채울수있는 형태 2개. 11
# N=6일땐 N이 4인경우를 처음 (0,0) 기준으로 집어넣고, 나머지를 N=2인경우로 채웠을때 11*3 +
# 또한 4일때만 만들 수 있는 형태 2개를 (0,2) 기준으로 넣어줄경우, 나머지를 N=2인경우로 채울수 있다. 3*2 +
# N=6일때만 채울수있는 형태도 2개다. 그래서 N=6일때는 33+6+2 = 41개
# 같은방식으로 N=8일때는 153, 41*3 + 2*11 + 3*2 + 2
# 6(일반+특수)+2, [4(특수)+4(일반), 4(일반)+4(특수)] 2+6(특수), 8일때만 채우는 형태 2
# i=8 , dp[8] = dp[6]*3 + dp[4]*2 + dp[2]*2 + dp[0]*2
# 같은 방식으로 i=10인경우는 아마
# dp[8]*3 + dp[6]*2 + dp[4]*2 + dp[2]*2 + dp[0]*2 일 것이다.

N=int(input())
dp=[0]*(N+1)

dp[0]=1
dp[1]=0 # N이 1일때
if(N>1):
    dp[2]=3 # N이 2일때

for i in range(3,N+1):
    if(i%2==0):
        dp[i]=dp[i-2]*3
        for j in range(4, i+1, 2):
            dp[i]+=dp[i-j]*2 # *2씩 되는 구간은 i-4 이하 짝수

print(dp[N])
