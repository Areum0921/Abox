# bfs
# 맵이 정사각형이 아님!! -> 문제를 제대로 보자
from collections import deque
def bfs(x,y,maps,check):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    #print("?",check)
    q=deque()
    q.append([x,y])

    while q:
        a,b=q.popleft()
        for i in range(4):
            ax=a+dx[i]
            bx=b+dy[i]
            if(0<=ax<len(maps) and 0<=bx<len(maps[0]) and maps[ax][bx]==1 and check[ax][bx]==1):
                check[ax][bx]=check[a][b]+1
                q.append([ax,bx])

    print(check)

def solution(maps):
    answer = -1
    loc=len(maps)-1
    loc2=len(maps[0])-1
    print(loc,loc2)
    check = [[1] * len(maps[0]) for i in range(len(maps))]
    print(check)
    bfs(0,0,maps,check)
    if(check[loc][loc2]>1):
        answer=check[loc][loc2]
    print(answer)
    return answer


maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1]]
solution(maps)
