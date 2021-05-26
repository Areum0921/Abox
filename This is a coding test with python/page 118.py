# 방향 전환 함수 만들기
#

def turn_left():  # 왼쪽 방향으로 회전하기
    global d
    if d == 3:  # 서쪽방향일때 북쪽방향으로
        d = 0
    else:
        d += 1
    return d

def solution(A,B,d,board):
    dx=[0,1,0,-1]
    dy=[-1,0,1,0] # 북 동 남 서

    board[A][B]=1 # A,B 방문처리
    cnt=1
    turn=0 # 몇번 회전했는지
    while 1:
        direction = turn_left()
        x=dx[direction]+A
        y=dy[direction]+B
        if 0<=x<len(board[0]) and 0<=y<len(board) and board[x][y]==0: # 해당 방향으로 이동할 수 있으면 이동
            board[x][y]=1 # 방문 체크
            A=x # 좌표 이동
            B=y # 좌표 이동
            turn=0
            cnt+=1
        else:
            turn+=1
        if turn==4: # 해당 자리에서 4턴은 초기 방향으로 돌아온 것, 즉 갈 수 있는곳이 없음.
            break

    print(cnt)


A,B = 1,1 # 시작좌표
d=0 # 방향  0: 북 , 1: 동, 2: 남, 3: 서
board=[[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]

solution(A,B,d,board)
