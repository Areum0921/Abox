n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    graph[i][i]=0 # a->a로 이동하는 비용 0

for i in range(m):
    a,b,c = map(int,input().split(" "))
    graph[a][b] = min(graph[a][b],c) # a->b 노선이 한개가 아닐 수 있다. 기존노선보다 작은값


# 플로이드 워셜 점화식 알아두기
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])


for i in range(1,len(graph)): # 갈수있는 경로가없는경우 INF인데, 0으로 바꿔준다.
    for j in range(1,len(graph)):
        if graph[i][j]==INF:
            graph[i][j]=0 # 1로 입력해놓고 틀린이유를 찾고있었다.
    print(' '.join(map(str, graph[i][1:]))) # 각 행마다 INF -> 0으로 바꿔준 후 출력


