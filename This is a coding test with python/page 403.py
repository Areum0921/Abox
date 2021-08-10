from collections import deque

INF = 1e9

n = int(input())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

board = []

size = 2 # 아기상어 크기 초기값
now_x, now_y = 0,0 # 아기 상어 위치 저장

for i in range(n):
    fish = list(map(int,input().split()))
    board.append(fish)
    if 9 in fish: # 아기 상어 시작 위치 저장
        now_x,now_y = i,fish.index(9)
        board[now_x][now_y] = 0

def bfs(): # 현재 위치에서 각 위치 까지 갈수있는 곳들의 최단거리 계산
    board_time = [[-1] * n for _ in range(n)]
    q=deque()

    q.append([now_x,now_y])
    board_time[now_x][now_y]=0 # 시작 위치

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]<=size and board_time[nx][ny]==-1: # 자기보다 작거나, 같은거만 지나갈수있음.
                    board_time[nx][ny] = board_time[x][y] + 1
                    q.append([nx,ny])

    return board_time

def check(board_time):
    min_time = INF
    x,y = 0,0
    for i in range(n):
        for j in range(n):
            if board_time[i][j] != -1 and 1 <= board[i][j] < size: # 갈 수있으면서, 먹을 수 있는 물고기
                if board_time[i][j] < min_time: # 제일 가까운곳부터 감.
                    x,y = i,j
                    min_time = board_time[i][j]

    if min_time == int(1e9):
        return False
    else:
        return x,y,min_time

answer = 0
ate = 0

while True:
    time = bfs()
    value = check(time) # x, y, min_time

    if value==False:
        print(answer)
        break
    else:
        now_x,now_y = value[0], value[1]
        answer += value[2]
        board[now_x][now_y] = 0 # 물고기 먹었으니 해당위치는 아무것도없음.
        ate += 1
        if ate == size: # 자신의 크기와 같은수 먹어야 크기 증가.
            size += 1
            ate = 0




