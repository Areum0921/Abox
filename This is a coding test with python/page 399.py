# 순서가 정해져있음 -> 위상정렬
from collections import deque

T = int(input())
for i in range(T):

    n=int(input())
    indegree=[0]*(n+1) # 진입 차수
    graph = [[False]*(n+1) for _ in range(n+1)]

    last_rank = list(map(int,input().split()))

    # 지난해 랭킹 진입차수
    for i in range(n):
        for j in range(i+1,n):
            #print(last_rank[i],last_rank[j])
            graph[last_rank[i]][last_rank[j]]=True # i팀이 j팀보다 높은 등수.
            indegree[last_rank[j]] += 1
    # 진입 차수가 낮은게 높은 등수 -> 진입차수 0 은 자신의 앞이 없음 -> 1등

    # 올해 변경된 순위 입력
    c = int(input())
    for i in range(c):
        a,b = map(int,input().split())

        # 순위가 바뀌었다는거는 간선을 뒤집으면 된다.
        # 현재 graph[a][b]를 뒤집어준다.
        if graph[a][b]: # ==True
            graph[a][b]=False # a -> b에서
            graph[b][a]=True # b -> a로 변경
            indegree[a] += 1 # a 진입 +1
            indegree[b] -= 1 # b 진입 -1
        else: # ==FALSE
            graph[a][b]=True
            graph[b][a]=False
            indegree[a] -= 1
            indegree[b] += 1
    print("new",graph)
    answer = []
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0: # 진입차수가 0인 노드 큐에 삽입후 시작
            q.append(i)

    check = False # 오직 1개의 위상정렬 여부
    cycle = False # 사이클 존재 여부

    for i in range(n):
        if len(q) == 0: # q가 비어있으면 사이클 발생
            cycle = True
            break
        if len(q) > 1: # q의 원소가 2개이상이면 위상정렬 결과 2개이상.
            # 원소가 2개이상이라는것은 현재 노드에서 2가지 방향으로 뻗어나갈 수 있기때문에 고정된 1개의 등수가 아님.
            check = True
            break

        now = q.popleft()
        answer.append(now)

        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j]==0:
                    q.append(j)

    if cycle==True: # 싸이클이 있다는건 데이터가 앞뒤가 안맞아 순위를 정할 수 없음
        print('IMPOSSIBLE')
    elif check==True: # 위상정렬이 2개이상인건 조건에 해당하는 순위가 여러개 나옴.
        print("?")
    else:
        for i in answer:
            print(i,end=' ')
        print()