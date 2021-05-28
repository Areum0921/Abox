# 1부터 해당 숫자까지 필요한 연산 횟수
# 26 = 25 5 1

def solution(N):
    dp=[0]*30001 # N의 범위 최대 30000

    for i in range(2,N+1): # 인덱스 0이 1이 아니라 인덱스 1이 1
        dp[i]=dp[i-1]+1

        if i%2==0:
            dp[i]=min(dp[i],dp[i//2]+1)
        elif i%3==0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        elif i%5==0:
            dp[i] = min(dp[i], dp[i // 5] + 1)

    print(dp[N])

solution(25)
