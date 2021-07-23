# A->B 점수 A<B
# B->A 점수 A>B

n,m=map(int,input().split(" "))
INF = int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i]=0

for i in range(m):
    a,b = map(int,input().split(" "))
    graph[a][b] = 1 # a < b


for i in range(1,n+1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])

answer = 0

for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if graph[i][j]!=INF or graph[j][i] != INF: # i<j or j<i
            # i가 j에 대해서 점수가 낮거나, 높음을 알 수 있는 경우가 n개와 같다면 등수를 알 수 있다.
            cnt+=1
    if cnt == n:
        answer += 1

print(answer)