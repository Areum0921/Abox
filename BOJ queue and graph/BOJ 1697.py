# 이동 하는 범위만 위,아래,오른쪽,왼쪽이 아닐뿐. 비슷한 문제가 많았다.
# bfs 이전에 방문했던곳은 다시 방문하지 않는다는 점을 생각하자.
from collections import deque
N,K = map(int,input().split(" "))
check=[0]*1000001 # 갔던곳인지 체크
dx = [-1,1,2]
check[N]=0
q=deque([])
q.append(N)
cnt=0
while q:
    x=q.popleft()
    if(x==K): # 탐색 중지.
        print(check[x])
        break
    for i in range(3): # 현재 위치에서 갈 수 있는곳 -1,1,*2
        if(i==2):
            a=x*dx[i]
        else:
            a=x+dx[i]
        if(0<=a<=100000 and check[a]==0):
            q.append(a)
            check[a]=check[x]+1

