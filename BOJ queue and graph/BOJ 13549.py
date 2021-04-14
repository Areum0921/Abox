# 순간이동은 0초
from collections import deque
N,K=map(int,input().split(" "))
check=[-1]*100001

q=deque()
q.append(N)
check[N]=0 # 처음 지점의 이동횟수 0

while q:
    x=q.popleft()
    if(x==K):
        print(check[K])
        break
    if(0<=x*2<=100000 and check[x*2]==-1): # 현재의 2배 지점을 방문 하지 않았을때
        check[x*2]=check[x]
        q.appendleft(x*2) # 순간이동은 0초라 가장 먼저 고려해야한다.
        # q맨 앞에 넣어서 순간이동 지점부터 다시 시작.
    if(0<=x+1<=100000 and check[x+1]==-1):
        check[x+1]=check[x]+1 # 현재 지점보다 이동횟수 + 1
        q.append(x+1)
    if(0<=x-1<=100000 and check[x-1]==-1):
        check[x-1]=check[x]+1 # 현재 지점보다 이동횟수 + 1
        q.append(x-1)


