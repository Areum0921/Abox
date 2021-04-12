import sys
input = sys.stdin.readline
N,M,V = map(int, input().split(" "))
s=[[0]*N for _ in range(M)]
check = [False]*N

for i in range(M):
    x,y=map(int, input().rstrip().split(" "))
    s[x-1][y-1]=1
    s[y-1][x-1]=1



def dfs(x): # dfs
    check[x]=True
    print(x+1,end=" ")
    for i in range(N):
        if(check[i]==False and s[x][i]==1):
            dfs(i)

def bfs(x):
    queue=[x]
    check[x]=False
    while(queue): # 큐가 모두 빌때까지 반복
        x = queue.pop(0)
        print(x+1,end=' ')
        for i in range(N):
            if(check[i]==True and s[x][i]==1):
                queue.append(i)
                check[i]=False # 방문처리

dfs(V-1)
print()
bfs(V-1)