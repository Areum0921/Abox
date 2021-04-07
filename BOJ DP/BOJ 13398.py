# DP를 2가지 경우로 나눠 저장한다. 1개의 숫자를 제거한경우, 아닌경우

N=int(input())
number=list(map(int,input().split(" ")))
dp=[[0]*2 for _ in range(N)]
dp[0][0]=number[0] # 숫자를 제외 하지 않은경우
dp[0][1]=number[0] # 숫자를 제외 한 경우
max_ans=number[0]

if(N>1):
    for i in range(1,N):
        dp[i][0]=max(number[i],dp[i-1][0]+number[i]) # 현재값과 이전값+현재값을 비교해서 큰 값으로 저장
        dp[i][1]=max(dp[i-1][0],dp[i-1][1]+number[i])
        # number[i]값이 제외된경우, number[i]값이 제외되지 않은경우
        # print(dp[i-1][0],dp[i-1][1]+number[i],number[i])

        max_ans=max(dp[i][0],dp[i][1], max_ans) # 가장 큰 값 갱신.

print(max_ans)
print(dp)

