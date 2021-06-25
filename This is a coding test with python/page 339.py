"""
input :
4 4 1 1
1 2
1 3
2 3
2 4
output :
2
3
"""
from collections import deque

N,M,K,X = map(int,input().split(" "))
graph = [[] for _ in range(N+1)]
dis = [-1] * (N+1)
dis[X]=0

for i in range(M):
    a,b = map(int,input().split(" "))
    graph[a].append(b)

q=deque() # 시작지점
q.append(X)

while q:
    cor = q.popleft()

    for i in graph[cor]:
        if dis[i]==-1:
            dis[i]=dis[cor]+1
            q.append(i)

cnt=0
for i in range(len(dis)):
    if dis[i]==K:
        cnt+=1
        print(i)

if cnt==0:
    print(-1)




"""
def solution(N,M,K,start,route):

    graph=[[] for _ in range(N+1)]
    dis=[-1]*(N+1)
    dis[start]=0 # 출발 도시

    for i in route:
        graph[i[0]].append(i[1])

    print(graph)

    q=deque([start])

    while q:
        cor = q.popleft() # 현재 도시 위치

        for next in graph[cor]:
            if dis[next]==-1:
                dis[next]=dis[cor]+1
                q.append(next)

    answer = dis.count(K)

    if answer==0:
        return -1
    else:
        return answer

N,M,K,X=4,4,2,1
route=[[1,2],[1,3],[2,3],[2,4]]
print(solution(N,M,K,X,route))

"""