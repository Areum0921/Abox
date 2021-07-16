#T = int(input())
gold = []
dp=[]
answer=0
n,m = map(int,input().split())

for i in range(n):
    gold.append(list(map(int,input().split(" "))))

for j in range(n):
    dp.append([gold[j][0]]) # 초기값 설정

for i in range(1,m): # 1열씩 최대값 구해나가기
    for j in range(n):
        if j==0: # 맨 위 좌표
            max_value = max(dp[j][i-1]+gold[j][i],dp[j+1][i-1]+gold[j][i])
        elif j==n-1: # 맨 아래 좌표
            max_value = max(dp[j][i - 1] + gold[j][i], dp[j - 1][i - 1] + gold[j][i])
        else: # 나머지 좌표
            max_value = max(dp[j][i - 1] + gold[j][i], dp[j - 1][i - 1] + gold[j][i], dp[j+1][i-1]+gold[j][i])

        dp[j].append(max_value) # 해당좌표의 최대값 
        answer = max(answer , max_value) # 저장된 answer, 방금계산한 값 중 큰값으로 저장

print(answer)

"""
input : 
3 4
1 3 3 2
2 1 4 1
0 6 4 7
output : 19

input :
4 4
1 3 1 5
2 2 4 1
5 0 2 3
0 6 1 2
output : 16
"""
