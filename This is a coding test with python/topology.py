# 선후 관계가 필요한 순서

from collections import deque

v,e = map(int,input().split(" "))

indegree=[0]*(v+1) # 진입 차수

graph=[[] for _ in range(v+1)]

print(graph)

for i in range(e): # 간선 정보
    a,b = map(int,input().split(" "))
    graph[a].append(b)
    indegree[b]+=1 # 진입 차수 증가 (b로 가는 경로)

def topology_sort():
    result=[]
    q=deque()

    for i in range(1,v+1):
        if indegree[i]==0: # 진입차수가 0인 노드를 큐에 삽입
            q.append(i)

    while q:
        now=q.popleft()
        result.append(now)

        for i in graph[now]: # now에 연결된 간선들
            indegree[i]-=1 # 진입차수 하나 감소

            if indegree[i]==0: # 감소해서 진입 차수가 0이 되면
                q.append(i) # 큐에 추가
    return result

print(topology_sort())