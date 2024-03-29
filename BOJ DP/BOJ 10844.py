dp=[[0]*10 for i in range(101)]

# 각자리수별로 0~9로 끝나는경우
dp[0]=[0,1,1,1,1,1,1,1,1,1]
dp[1]=[1,1,2,2,2,2,2,2,2,1]
dp[2]=[1,3,3,4,4,4,4,4,3,2]

#n자리수일때 0으로 끝나려면 n-1자리가 1로끝나야함, 1로 끝나려면 2or0으로끝나야함 , 2로 끝나려면 3or1로 끝나야함..
# 9로끝나려면 8로끝나야함
N=int(input())

for i in range(3,N):
    for j in range(10):
        if(j==0): # 0으로 끝날때
            dp[i][j]=(dp[i-1][j+1])%1000000000 # i-1자리에서 1로 끝나는 경우의 개수
        elif(j>=1 and j<=8): # 2~8로 끝날때
            dp[i][j]=(dp[i-1][j-1]+dp[i-1][j+1])%1000000000
        else:
            dp[i][j]=(dp[i-1][j-1])%1000000000 # i-1자리에서 8로 끝나는 경우의 개수

print(sum(dp[N-1])%1000000000)