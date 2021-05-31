# 한 도시에서 보낸 메세지가 도달 가능한 도시 수, 최대 걸리는 시간

import heapq

INF = int(1e9)

n,m,c = map(int,input().split(" ")) # 도시 수, 통로 수, 메세지를 보내는 도시

graph=[[] for _ in range(n+1)]

distance = [INF]*(n+1)

for i in range(m):
    x,y,z = map(int,input().split(" ")) # x->y 통로, 메세지를 보내는 시간 z
    graph[x].append((y,z)) # x도시에서 y도시로 메세지를 보냄. z 시간 걸림.

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) # 시작도시, 비용 0 큐에 넣기
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q) # 거리와, 도시
        if dist > distance[now]: # now로 가는 거리가 기존보다 크면 무시
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)

answer=0 # 도달 할 수 있는 도시 수
max_value=0 # 제일 긴 시간
for i in distance:
    if i!=INF: # 도달 할 수 있는 도시면
        answer+=1 # 도시 수 + 1
        max_value=max(max_value,i) # 메세지 보내는 시간 계산

print(answer-1, max_value)
