# 0이 있으면 -1, 처음부터 모든 토마토가 익어있으면 0
import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int,input().split(" "))
board=[list(map(int,input().split(" "))) for _ in range(M)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

q = deque([])

for i in range(M):
    for j in range(N):
        if(board[i][j]==1):
             q.append([i,j]) # 탐색해야할 시작 위치들을 q에 넣어주기.

cnt=-2
while(q):
    x, y = q.popleft()
    for i in range(4):
        a=x+dx[i]
        b=y+dy[i]
        if(0<=a<M and 0<=b<N and board[a][b]==0):
            q.append((a, b))
            board[a][b] = board[x][y]+1
            cnt=board[a][b]

for i in range(M):
    if(0 in board[i]): # 익힐 수 없는 토마토 있음.
        cnt=0

if(cnt==-2): # 처음에 다 익은 상태
    print(0)
else:
    print(cnt-1) # 가장 마지막 값





