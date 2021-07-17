# 가장 긴 내림차순 수열
N = int(input())
soldier = list(map(int,input().split(" ")))
dp = [1]*(N+1)


for i in range(1,N):
    for j in range(i):
        print(i,j)
        if soldier[j] > soldier[i]: # soldier[i]앞의값보다 큰값을 찾았을때
            dp[i] = max(dp[i],dp[j]+1)

print(N-max(dp)) # 전체 병사 수 - 가장 긴 내림차순 수열 길이



