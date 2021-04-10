# dfs를 여러번 반복하면 된다. 시작점으로부터 이어진게 끝날때 까지 탐색이다. 즉 1 dfs 실행 = 연결요소 1개
# a-> a도 하나의 경로이라 여겨야함... a로 가는길이 없다면 a->a 자체가 간선을 0개 이용하는 하나의 경로
# 이 부분 때문에 시간을 많이 먹음
import sys
limit_number=10000
sys.setrecursionlimit(limit_number)

N,M=map(int,sys.stdin.readline().strip().split(" "))
connected=[[0] * (N+1) for _ in range(N+1)]
check=[False]*(N+1)

for i in range(M):
    a,b=map(int,sys.stdin.readline().strip().split(" "))
    connected[a][b]=connected[b][a]=1


def dfs(x):
    check[x]=True
    for i in range(1,N+1):
        if(check[i]==False and connected[x][i]==1):
            dfs(i)

cnt=0
for i in range(1, N+1):
    if(check[i]==False):
        dfs(i)
        cnt+=1

print(cnt)
