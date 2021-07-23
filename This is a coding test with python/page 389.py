# 다익스트라
import heapq

INF = int(1e9)
N = int(input())
graph = []
dis = [[INF]*N for i in range(N)]
for i in range(N):
    graph.append(list(map(int,input().split(" "))))

dx = [-1,0,1,0] # 상하좌우 1칸
dy = [0,-1,0,1]

s, e = 0,0 # 시작 위치

q=[(graph[s][e],s,e)]
dis[s][e] = graph[s][e] # 시작위치 비용

while q:
    cost, s, e = heapq.heappop(q)

    if dis[s][e] < cost: # 기존에 기록된 비용보다 크면 탐색 x
        continue

    for i in range(4):
        ns = s+dx[i]
        ne = e+dy[i]
        if 0<=ns<N and 0<=ne<N: # 이동 가능한 좌표면
            new_cost = cost + graph[ns][ne] # 그곳으로 이동했을때 지금 좌표까지 비용 + 해당좌표 비용
        else:
            continue
        if new_cost<dis[ns][ne]: # 기존비용 보다 작으면 갱신
            dis[ns][ne] = new_cost
            heapq.heappush(q, (new_cost,ns,ne))
    print("@@@@@@@@@@@@@@@@@@@@@@")
    for j in dis:
        print(j)

print(dis[N-1][N-1])
