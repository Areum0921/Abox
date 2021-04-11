import sys

N=int(sys.stdin.readline().strip())
board=[list(map(int,sys.stdin.readline().rstrip())) for i in range(N)]
check=[[0]*N for i in range(N)]
#print(board)
#print(check)
dx=[1,0,-1,0] # 동남서북
dy=[0,-1,0,1]
cnt=0

def dfs(x,y):
    global cnt # 1단지당 집 개수
    check[x][y]=1 # 방문 표시
    if(board[x][y]==1):
        cnt+=1
    for i in range(4): # 이부분이 중요하다. 다양한 문제에서 나오는 4방향으로 탐색하는 방법!!
        nx = x+dx[i]
        ny = y+dy[i]
        if((nx>=0 and nx<N) and (ny>=0 and ny<N)): # 살필 수 있는 좌표 범위 [0~n][0~n]
            if(check[nx][ny]==0 and board[nx][ny]==1):
                dfs(nx,ny)

cnt_list=[] # 단지별 집 수
for i in range(N):
    for j in range(N):
        if(check[i][j]==0 and board[i][j]==1): # 방문 안했으면서 해당 위치에 집이 있을때
            dfs(i,j) # 탐색 시작 좌표
            cnt_list.append(cnt)
            cnt=0

print(len(cnt_list))
cnt_list.sort()
for i in range(len(cnt_list)):
    print(cnt_list[i])
