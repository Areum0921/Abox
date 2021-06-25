from collections import deque
N,K=map(int,input().split(" "))
board = []
virus_data=[]
for i in range(N):
    virus=list(map(int,input().split(" ")))
    board.append(virus)
    for j in range(N):
        if board[i][j]!=0:
            virus_data.append((board[i][j],0,i,j)) # 종류, 시간, 좌표

virus_data.sort()
q = deque(virus_data)
S,X,Y = map(int,input().split(" "))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

while q:
    virus_num,time,x,y = q.popleft()
    if time == S:
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and board[nx][ny]==0:
            board[nx][ny]=virus_num
            q.append((virus_num,time+1,nx,ny))


print(board[X-1][Y-1])
