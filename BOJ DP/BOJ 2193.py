# 끝이 0인 경우는 1,0 붙일수있음, 1로 끝나는경우 0만 추가가능

dp=[[0] * 2 for _ in range(100)]
dp[1]=[0,1]
dp[2]=[1,0]
dp[3]=[1,1]

N=int(input())
for i in range(4,N+1):
    dp[i][0]=dp[i-1][0]+dp[i-1][1] # 0으로 끝나려면 이전꺼의 1로끝나는경우,0으로끝나는경우
    dp[i][1]=dp[i-1][0] # 1로 끝나려면 이전꺼의 0으로 끝나는경우

print(sum(dp[N]))