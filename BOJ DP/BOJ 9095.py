# 규칙 찾기
# 각 수를 만들 수 있는 순열의 합
# EX)5
# 1 -> 5개 5P5 = 1
# 1 -> 3개 2 -> 1개 4P3 + 1P1 = 4
# 1 -> 1개 2 -> 2개 1P1 + 3P2 = 3
# 1 -> 2개 3 -> 1개 3P2 + 1P1 = 3
# 2 -> 1개 3 -> 1개 2P1 + 1P1 = 2
# dp[1]=1, dp[2]=2, dp[3]=4, dp[4]=7, dp[5]=13
# dp[i]=dp[i-3]+dp[i-2]+dp[i-1]

dp=[0,1,2,4]
for i in range(4,11): # n은 양수이며 11보다 작음
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])

T=int(input())
for i in range(T):
    number=int(input())
    print(dp[number])