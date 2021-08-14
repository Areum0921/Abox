# 마을 개수, 도로정보, 배달가능시간.
# 시작점은 1번마을
# 다익스트라 우선순위큐 사용
import heapq

def solution(N, road, K):
    INF = int(1e9)
    dis=[INF]*(N+1)
    graph = [[]*(N+1) for _ in range(N+1)]
    answer = 0

    for i in road:
        a,b,c = i
        graph[a].append([b,c])
        graph[b].append([a,c])

    dis[1] = 0 # 1번마을은 시작점
    q=[(0,1)] # cost, start

    while q:
        cost, now = heapq.heappop(q)

        for i in graph[now]:
            if dis[i[0]] < cost: # 기존 경로보다 더해야할 cost 자체가 높으면 계산할 필요 x
                continue
                
            if dis[i[0]] > cost+i[1]: # 기존 경로보다 더 작은 비용이면
                dis[i[0]] = cost+i[1]
                heapq.heappush(q,[cost+i[1],i[0]])

    for i in range(1,len(dis)):
        if dis[i]<=K:
            answer+=1

    return answer

N=5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
solution(N,road,K)