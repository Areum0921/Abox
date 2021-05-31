INF = int(1e9)

n,m = map(int,input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1): # 자기 자신으로 가는 거리(비용)은 0
    graph[i][i] = 0

for _ in range(m): # 간선에 대한 정보 입력
    a,b,c = map(int,input().split())
    graph[a][b]=c


for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k]) # 기존 j->k 값과 j->i->k값 비교

for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j],end=" ")

