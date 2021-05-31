# 개선된 다익스트라는 힙 자료구조를 사용. (n log n)
# 파이썬에서 PriorityQueue, heapq 가 우선순위 큐 기능을 지원
# heapq가 더빠름.
# 기본적으로 최소힙인데, 다익스트라는 적은 비용 노드 우선이기때문에 적합하다.
# 최소힙을 최대힙처럼 사용하려면 -를 붙였다가 큐에서 꺼낼때 다시 -를 붙여 값을 돌리는 방식 이용.

import heapq

INF=int(1e9)

n,m=map(int,input().split()) # 노드, 간선 개수

start=int(input()) # 시작 노드 번호

graph= [[] for i in range(n+1)] # 각 노드에 연결된 노드 정보

visited=[False] * (n+1) # 방문 체크

distance = [INF] * (n+1) # 최단거리(비용) 저장용

for _ in range(m): # 간선 입력
    a, b, c = map(int,input().split()) # a노드 -> b노드 , 거리(비용) c
    graph[a].append((b,c))

print(graph)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # 큐에 시작지점은 경로 0으로 삽입
    distance[start]=0 # 시작점은 거리(비용) 0

    while q:
        print(distance)
        # 최소힙이라, 맨앞 노드가 최단 거리(비용)가 짧은 노드.
        dist,now = heapq.heappop(q) # q에서 거리(비용)과, 노드를 꺼낸다.
        if distance[now] < dist: # 이미 저장된 거리(비용)이 더 작으면 무시
            continue

        for i in graph[now]: # now에 인접한 노드들 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])