N=int(input())
nlist=list(map(int,input().split(" ")))

dp=[0]*N
dp[0]=nlist[0]

for i in range(1,N):
    dp[i]=nlist[i]
    for j in range(i):
        if(nlist[j]<nlist[i] and dp[i] < dp[j]+nlist[i]):
            dp[i]=dp[j]+nlist[i]
        print(dp)
#ex)30 20 10 40일때,
# dp[i]의 초기값은 nlist[i]
# 20, 10은 내림차순이니 패스 dp[1]=20,dp[2]=10
# 40일때 nlist[0]<nlist[3] 이고 dp[3]<dp[0]+nlist[3] 이다.30<40, 30<30+40
# 그럼 dp[3] 을 dp[0]+nlist[3]= 70으로 갱신
# 다음으로 nlist[1]<nlist[3]이나, dp[3]<dp[1]+nlist[3]이 거짓이다. 20<40 , 70 < 20+40
# 같은방식으로 반복해서 dp값중 max값을 찾아주면된다.
print(max(dp))
