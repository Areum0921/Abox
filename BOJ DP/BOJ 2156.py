# 포도주가 총 N잔일때
# N이 홀수 일때 :
import sys

N=int(sys.stdin.readline())
wine=[]
dp=[0]*(N+2)

for i in range(N):
    wine.append(int(sys.stdin.readline()))

dp[0]=wine[0]  # 첫째 잔까지 마실때
if(N>1):
    dp[1]=wine[0]+wine[1] # 둘째 잔까지 마실때

if(N>1):
    for i in range(2,N):
        dp[i]=max(dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i])
        # 연속 최대 2잔, 현재잔+전전잔까지의 최대값 or 전전전잔까지의 최대값 + 현재,현재전잔
        # ex) 8번째 잔을 마시려면 6번째잔까지의 max+8째잔 or 5번째잔까지의 max+7,8번째잔
        dp[i]=max(dp[i-1],dp[i])
        # 연속으로 마시지 않을경우

print(dp[N-1])

