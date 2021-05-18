# 7,8,9 시간초과 -> 인접리스트를 이용해야한다.
# 그래프 문제 해결은 딕셔너리를 이용
from collections import deque

def solution(n, edge):
    answer = 0
    check=[-1]*(n+1)
    link=dict()
    for i,j in edge: # 각 노드에 대해 연결된 노드 정리
        link.setdefault(i,[]).append(j)
        link.setdefault(j,[]).append(i)

    print(link)
    q=deque([[1,0]]) # node, 거리
    print(q)

    while q:
        x,y=q.popleft()
        check[x]=y
        for i in link[x]: # 노드 x에 연결된 좌표들
            if check[i]==-1: # 해당 좌표에 방문한적이 없으면
                check[i]=check[x]+1 # 현재 노드 + 1 거리
                q.append([i,y+1])# 노드 i와, 거리 1증가 큐에 넣기.

    print(check)
    answer = check.count(max(check))
    return answer


n=6
edge=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n,edge)