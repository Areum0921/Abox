# 경로를 고려해야 하기 때문에 플로이드 워셜 이용.
# 1번노드 출발 -> K번 회사 -> X번 회사
INF = int(1e9)

n,m = map(int,input().split(" "))

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i]=0 # 자기 자신으로 가는 비용 0

for i in range(m):
    a,b=map(int,input().split(" ")) # a->b 비용은 1
    graph[a][b]=1 # 양방향 처리 a->b == b->a
    graph[b][a]=1

x,k = map(int,input().split(" "))

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

#print(graph)
if graph[1][k]!=INF and graph[k][x]!=INF:
    print(graph[1][k]+graph[k][x]) # k에 갔다가 x로 가야함.
else:
    print(-1)


