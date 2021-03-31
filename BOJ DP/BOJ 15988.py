#python3 시간초과 -> pypy3 통과
dp=[0]*1000001
# n이 5일때 4로끝나는경우에 1더하기, 3으로 끝나는경우에 2더하기, 2로끝나는 경우에 3더하기
dp[1]=1
dp[2]=2
dp[3]=4

def solution(N):
    for i in range(4,N+1):
        dp[i]=(dp[i-3]+dp[i-2]+dp[i-1])%1000000009
    return dp[N]


T=int(input())
for i in range(T):
    N=int(input())
    if(dp[N]!=0):
        print(dp[N])
    else:
        print(solution(N))


