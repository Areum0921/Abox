# 분명 답이 잘나오는데 실패가 떴다.
# 입력부분을 테스트 케이스때 반복마다 넣지 않고 실행했으면서 왜틀렸는지 이해를 못했다..
# 기본이 중요. 문제를 잘 보고 조건을 잘 살피자.
import sys
input = sys.stdin.readline

T=int(input())

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(x,y):

    check[x][y]=True # 방문 표시
    for i in range(4):
        a = x+dx[i]
        b = y+dy[i]
        if(0 <= a < M and 0 <= b < N): # 4방향 탐색
            if(board[a][b]==1 and check[a][b]==False): # 지렁이가있고, 가지 않았다면
                dfs(a,b)

for k in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * N for i in range(M)]  # 빈 배추밭 생성
    check = [[False] * N for i in range(M)]  # 방문 체크
    cnt=0 # 지렁이 개수 카운트

    for i in range(K):
        x, y = map(int, input().split(" "))  # 배추 위치 입력
        board[x][y] = 1


    for i in range(M):
        for j in range(N):
            if(check[i][j]==False and board[i][j]==1):
                dfs(i,j)
                cnt+=1
    print(cnt)


