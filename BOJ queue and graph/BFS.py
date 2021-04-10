# 탐색의 기초인 bfs가 어떤식으로 돌아가는지 알기 위해 작성.
N,y,v=map(int,input().split(" "))
list=[[0]*(N+1) for _ in range(N+1)]
check=[True]*(N+1)
for i in range(y):
    a,b=map(int,input().split(" "))
    list[a][b]=1
    list[b][a]=1 # 연결관계 표시
qlist=[]
cnt=0
def bfs(x):
    global cnt

    queue=[x]
    print('x값 %d'%x,'을 큐에 넣습니다.')
    print('현재큐 : ',queue)
    check[x]=False
    print('x값 %d'%x,'에 방문 표시합니다.')
    print('현재 방문 여부 : ',check)
    while(queue):
        print('큐의 제일 앞 숫자를 빼 출력합니다.',queue)
        cnt+=1
        x=queue.pop(0)
        print(x, end=' ')
        qlist.append(x)
        print()
        if(cnt==x):
            print('모든 탐색이 끝났습니다. bfs 결과 : ', qlist)
        else:
            print('다음으로 %d 와(과) 이어져 있는 숫자중 작은 숫자를 찾습니다.' % x)
        for i in range(N+1):
            if(check[i]==True and list[x][i]==1):
                print('숫자',i,'는(은) 방문하지 않았고',x,i,'는 연결되어있습니다.')
                queue.append(i)
                print(i,'를 큐에 저장합니다.')
                check[i]=False

bfs(v)
"""
def bfs(x):
    queue=[x]
    check[x]=False
    while(queue):
        x=queue.pop(0)
        print(x+1, end=' ')
        for i in range(N):
            if(check[i]==True and link[x][i]==1):
                queue.append(i)
                check[i]=False
                """