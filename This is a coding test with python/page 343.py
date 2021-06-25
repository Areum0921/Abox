# 벽을 세우는 모든 경우의 수에 대해서 깊이 or 너비 탐색으로 바이러스를 퍼트린후 안전영역 계산
N, M = map(int, input().split(" "))
board = [] * N
temp = [[0]*M for _ in range(N)]
answer = 0
for i in range(N):
    a = list(map(int, input().split(" ")))
    board.append(a)

def spread(x,y): # 바이러스 퍼트리기
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny]==0:
                board[nx][ny]=2 # 바이러스 배치
                spread(nx,ny)

def count_safety():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j]==0:
                cnt+=1
    return cnt

def solution(cnt):

    global answer

    if cnt == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = board[i][j] # 벽을 세운 임시 맵

        for i in range(N): # 벽을 세운 임시 맵에서 바이러스 퍼트리기
            for j in range(M):
                if temp[i][j]==2:
                    spread(i,j)
        print("?",count_safety())
        answer = max(answer,count_safety())
        return

    for i in range(N): # 벽 세우기
        for j in range(M):
            if board[i][j]==0: # 0 만나면 벽 세우기
                board[i][j]=1
                cnt +=1 # 벽 개수증가
                solution(cnt) # 재귀 (다시 실행될때 벽 3개면 위 코드 부분 실행)
                board[i][j]=0
                cnt-=1

    print(answer)

solution(0)

