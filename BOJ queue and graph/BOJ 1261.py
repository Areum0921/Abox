from collections import deque

M,N = map(int,input().split(" "))
board=[list(map(int,input())) for _ in range(N)]
check=[[-1]*M for _ in range(N)] # 벽 뚫는 수 기록용

dx=[0,1,0,-1]
dy=[1,0,-1,0]
q=deque()
q.append([0,0])
check[0][0]=0 # 시작점, 시작은 벽 0개뚫음

while q:
    x,y=q.popleft()
    for i in range(4):
        a=x+dx[i]
        b=y+dy[i]
        if(0<=a<N and 0<=b<M):
            if(check[a][b]==-1): # 방문하지 않은 경우
                if(board[a][b]==1): # 벽이 있으면
                    check[a][b]=check[x][y]+1 # 벽 뚫을때 x,y좌표 까지 뚫은벽 수 저장.
                    q.append([a,b])
                elif(board[a][b]==0):# 벽이 없으면
                   check[a][b]=check[x][y]
                   q.appendleft([a,b])

print(check[N-1][M-1])
