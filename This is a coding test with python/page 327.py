# 현재 뱀이 차지하는 위치는 큐로.
N=int(input()) # N*N 보드 크기
K=int(input()) # 사과 개수
board=[[0]*(N+1) for i in range(N+1)]
board[0][0]=2 # 뱀 표시
for i in range(K):
    x,y=map(int,input().split()) # 사과 위치 입력
    board[x][y]=1 # 사과 표시

command=[] # 방향 정보
L=int(input())
for i in range(L):
    x,c = map(str,input().split(" "))
    command.append((int(x),c)) # 시작 후 x초가 끝난 뒤 c방향 으로 전환

dx=[0,1,0,-1] # 동,남,서,북 
dy=[1,0,-1,0] # 인덱스 증가는 오른쪽방향, 감소는 왼쪽방향

def turn(direction,c):
    if c=='D':
        direction = (direction+1)%4
    else:
        direction = (direction-1)%4
    return direction

def solution():
    time, index=0,0 # 시간, 회전정보
    x,y = 1,1 # 뱀의 초기 위치
    board[x][y]=2 # 뱀이 있는 위치
    direction=0 # 초기방향 오른쪽(동)

    q=[(x,y)] # 뱀이 있는 위치.

    while 1:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1<=nx<=N and 1<=ny<=N and board[nx][ny]!=2: # 이동할 수 있고, 뱀의 몸통이랑 닿지 않으면
            if board[nx][ny]==1: # 사과가 있는경우
                board[nx][ny]=2 # 뱀이 위치함 표시
                q.append((nx, ny))  # 머리, 꼬리

            else: # 사과가 없는경우
                board[nx][ny]=2 # 뱀 위치표시
                q.append((nx,ny))
                px,py=q.pop(0) # 뱀 꼬리부분 제거
                board[px][py]=0 # 이전 위치 뱀표시 제거
        else: # 몸통에 닿거나, 벽이면
            time+=1 # time 반영하고 멈춤
            return time

        x,y=nx,ny # 뱀의 위치 갱신
        time+=1 # 시간 증가

        if index<L and time==command[index][0]: # 방향 전환할때 되면
            direction=turn(direction,command[index][1])
            index+=1

    return time

print(solution())