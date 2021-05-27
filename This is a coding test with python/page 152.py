# 최소 칸의 개수 = Bfs
from collections import deque

def bfs(board,x,y):
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]

    q=deque()
    q.append([x,y])

    while q:
        a,b=q.popleft()

        for i in range(4):
            ax=a+dx[i]
            by=b+dy[i]
            if 0<=ax<len(board) and 0<=by<len(board[0]) and board[ax][by]==1:
                q.append([ax,by])
                board[ax][by]=board[a][b]+1
    N=len(board)-1
    M=len(board[0])-1

    print(board[N][M])

board=[[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
bfs(board,0,0)


