# 1697에서 방문 기록만 추가해주면 된다.
from collections import deque
N,K = map(int,input().split(" "))
check=[0]*1000001 # 갔던곳인지 체크
path=[0]*1000001 # 이동 경로 저장
dx = [-1,1,2]
check[N]=0
q=deque([])
q.append(N)
cnt=0
path[N]=-1
while q:
    x=q.popleft()
    if(x==K): # 탐색 중지.
        print(check[x])
        p =[]
        while(x!=N):
            p.append(x) # 마지막 방문지 x 부터 넣고, 경로를 하나씩 넣음.
            x=path[x]
        p.append(N)
        p.reverse()
        print(' '.join(map(str,p)))

    for i in range(3): # 현재 위치에서 갈 수 있는곳 -1,1,*2
        if(i==2):
            a=x*dx[i]
        else:
            a=x+dx[i]
        if(0<=a<=100000 and check[a]==0):
            q.append(a)
            check[a]=check[x]+1
            path[a]=x # a로 오기전에 x를 방문.


