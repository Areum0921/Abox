# 규칙 찾기
# ex) 50 20 40 70 60 50 60일때
# dp[1]=1 // 50까지 길이는 1
# dp[2]=1 // 20까지 증가하는 수열길이는 1
# dp[3]=2 // 40미만 앞의 숫자중 dp값이 1보다 크거나 같은값의+1로 dp[3]갱신 , dp[3]= dp[2]+1 = 2
# dp[4]=3 // 70미만 앞의 숫자중 50일때 dp[1]+1해서 2, 40일때 dp[3]+1 해서 3
# dp[5]=3 // 60미만 앞의 숫자중 가장큰 dp값에 +1 , dp[3]+1 = 3
# dp[6]=3 // 50미만 앞의 숫자중 가장큰 dp값에 +1 , dp[3]+1 = 3
# dp[7]=4 // 60미만 앞의 숫자중 가장큰 dp값에 +1 , dp[6]+1 = 4
N=int(input())
dp=[1]*1001
numberlist=list(map(int, input().split(" ")))
dp[1]=1

for i in range(1,N):
    for j in range(i):
        #print(i,j)
        if(numberlist[j]<numberlist[i] and dp[j]>=dp[i]):
            dp[i]=dp[j]+1

max_numlist_idx=dp.index(max(dp)) # 제일 긴 수열의 마지막 값 위치찾기
max_dp_idx=dp[max_numlist_idx] # 제일 큰 dp값
max_list=[]

for k in range(max_numlist_idx-1,-1,-1): # dp 값이 하나씩 줄어들때마다 앞의 숫자임
    if(max_dp_idx==dp[k]+1):
        max_dp_idx=dp[k]
        max_list.insert(0,numberlist[k])
#ex) 입력이
# 7
# 5 2 4 7 6 5 6 일때 dp=[1,1,2,3,3,3,4]
# 제일 긴 수열의 마지막 값은6, 위치는 6
# dp[6]=4, 6 앞에 dp[n]=3인경우 넣기, dp[n]=2인경우 넣기... 반복 n=1까지
max_list.append(numberlist[max_numlist_idx])
print(max(dp))
print(" ".join(map(str, max_list)))


