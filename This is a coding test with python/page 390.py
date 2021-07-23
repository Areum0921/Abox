import heapq
N,M = map(int,input().split( ))
INF = int(1e9)
graph=[[]*(N+1) for _ in range(N+1)]
dis = [INF]*(N+1)

for i in range(M):
    a,b = map(int,input().split( ))
    graph[a].append(b) # a에 연결된 헛간들
    graph[b].append(a) # 양방향 통로

start = 1
q=[(0,start)] # 초기 비용, 시작점
dis[1] = 0 # 1 -> 1 은 거리 0
while q:
    dist,x = heapq.heappop(q)
    for i in graph[x]: # x에서 갈수있는 헛간들
        #print(x,"에서 갈수있음",i)
        if dis[i] < dist:
            continue
        new_dist = dist + 1
        #print("new",new_dist)
        if new_dist < dis[i]:
            dis[i] = new_dist
            heapq.heappush(q,(new_dist,i))


max_dis = max(dis[1:]) # 가장 긴거리
print(dis.index(max_dis),max_dis,dis.count(max_dis))
# 앞 인덱스부터 찾으므로 제일 작은 수, 가장 긴 거리, 해당 거리를 가진 값 개수


