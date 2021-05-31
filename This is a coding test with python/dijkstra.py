# 시간복잡도 O(n^2) 다익스트라 -> 이 방법은 시간이 오래걸려 코테 준비에 적합하지 않다.

INF=int(1e9)

n,m=map(int,input().split()) # 노드, 간선 개수

start=int(input()) # 시작 노드 번호

graph= [[] for i in range(n+1)] # 각 노드에 연결된 노드 정보

visited=[False] * (n+1) # 방문 체크

distance = [INF] * (n+1) # 최단거리(비용) 저장용

for _ in range(m): # 간선 입력
    a, b, c = map(int,input().split()) # a노드 -> b노드 , 비용 c
    graph[a].append((b,c))

print(graph)

def get_smallest_node():
    min_value=INF
    index = 0 # 최단 거리가 짧은 노드
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]: # 방문하지 않은 i로 가는 거리(비용)가 min_value보다 작을때
            min_value = distance[i] # min_value 갱신
            index = i # 현재 위치는 i노드
    return index

def dijkstra(start):
    distance[start]=0 # 시작점은 거리(비용) 0
    visited[start]=True # 시작점 방문 처리

    for j in graph[start]: # start 지점에서 갈 수 있는 노드
        distance[j[0]] = j[1] # j[0]으로 가는 거리(비용) j[1]

    for k in range(n-1): # 시작 노드 제외 나머지 노드 탐색
        now = get_smallest_node()
        visited[now]=True

        for m in graph[now]: # now에서 이동가능한 노드들
            cost = distance[now] + m[1] # 현재 now로 가는 비용 + now지점에서 m[0]으로 가는 거리(비용)
            if cost < distance[m[0]]: # 위 값이 기존 m[0]으로 가는 거리(비용)보다 작으면
                distance[m[0]] = cost # 새로운 거리(비용)으로 갱신

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])