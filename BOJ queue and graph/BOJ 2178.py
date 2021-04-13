# dfs로 풀려했으나, bfs 문제라고한다.
# 구분하는 방법은 계속 풀어봐야 느끼겠지만
# 그래프에서 모든 정점을 탐색하는 용도는 둘다 사용해도된다.
# 단! 가중치 없는 그래프의 최단 경로 문제는 only BFS <--- 중요
# 아직은 잘 모르겠지만, 여러 bfs,dfs 문제들을 풀다보면 구분할 수 있을지도

from collections import deque

N,M=map(int,input().split(" "))
miro = [list(map(int,input())) for _ in range(N)]
q=deque()

dx=[0,1,0,-1]
dy=[1,0,-1,0]
miro[0][0]=1 # 1,1에서 출발 한다는 조건으로 처음 시작지는 무조건 1

q.append([0,0]) # 처음 시작지 1,1의 인덱스

while(q):
    #print(miro)
    a,b = q[0][0], q[0][1]
    q.popleft() #큐 맨앞 빼기
    for i in range(4): # 이동할 수 있는 위치 찾기
        x=a+dx[i] # 현재 x 좌표에서
        y=b+dy[i] # 현재 y 좌표에서
        if(0<=x<N and 0<=y<M and miro[x][y]==1): # 좌표상 이동가능하고, miro에서 이동할수있는 1일때
            q.append([x,y]) # q에 넣어주기
            miro[x][y] = miro[a][b]+1 # 이동한 칸수 1씩 증가

print(miro[N-1][M-1])

