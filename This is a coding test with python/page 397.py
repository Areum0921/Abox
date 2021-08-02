# 크루스칼 알고리즘. 각 간선의 정보를 받아, cost값이 낮은 간선부터 이어나간다.
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,x,y):
    a = find_parent(parent,x)
    b = find_parent(parent,y)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a

N,M = map(int,input().split())

parent = [0]*N
for i in range(N):
    parent[i]=i

edges = [] # 간선정보
answer = 0
total = 0
for i in range(M):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b)) # 비용기준으로 정렬해야해서 cost가 맨 앞

edges.sort() # 비용기준 정렬

for i in edges:
    cost, a, b = i
    total+=cost # 모든 가로등을 켰을경우 비용
    # 모든 간선에 대해서 사이클 발생여부 확인 find_parent 이용
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b) # 사이클이 발생하지않으면 이어서 하나의 집합으로 합치기
        answer+=cost # 최소한의 필요 금액


# 정답은 절약금액임!
print(total-answer)
