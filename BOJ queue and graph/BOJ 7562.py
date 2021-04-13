import sys
input = sys.stdin.readline
from collections import deque
T=int(input())
for i in range(T):
    size=int(input())
    board=[[0]*size for i in range(size)]
    start=list(map(int,input().split(" ")))
    destination=list(map(int,input().split(" ")))
    dx=[-2,-1,1,2,-2,-1,1,2]
    dy=[1,2,2,1,-1,-2,-2,-1]

    q=deque([])
    q.append([start[0],start[1]]) # 스타팅 포인트 부터 이동가능한 칸으로 이동

    cnt=0
    while q:
        x,y=q.popleft()
        for i in range(8):
            a=x+dx[i]
            b=y+dy[i]
            if(0<=a<size and 0<=b<size and board[a][b]==0):
                q.append([a,b])
                board[a][b]=board[x][y]+1 # 한번이동할때마다 +1씩 증가한 숫자를 넣어준다.

    if(destination[0]==start[0] and destination[1]==start[1]):
        # 시작좌표와 목적좌표가 같으면 0
        print(0)
    else: # 시작좌표부터 출발하여 각 좌표에 도달하려면 움직여야하는 최소 횟수들을 저장해놈
        print(board[destination[0]][destination[1]])
