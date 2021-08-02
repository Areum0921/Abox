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

N=int(input())

parent=[0]*(N+1)

for i in range(1,N+1):
    parent[i]=i

# 각 좌표값에 대하여 행성간 거리를 계산 후, 행성을 일렬로 나열
x,y,z=[],[],[]
for i in range(1,N+1):
    a,b,c=map(int,input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))

x.sort() # 각 행성의 x좌표 순서대로 나열
y.sort() # 각 행성의 y좌표 순서대로 나열
z.sort() # 각 행성의 z좌표 순서대로 나열
# 행성 A,B 간의 거리 = min(abs(Ax-Bx),abs(Ay-By),abs(Az-Bz)) 인접행성끼리의 거리만 계산하면된다.

edges=[]
answer=0
for i in range(N-1):
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1])) # i+1 행성과 i 행성의 x좌표 거리, i번째 행성번호, i+1번째 행성번호
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))  # i+1 행성과 i 행성의 y좌표 거리, i번째 행성번호, i+1번째 행성번호
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))  # i+1 행성과 i 행성의 z좌표 거리, i번째 행성번호, i+1번째 행성번호

edges.sort() # 비용 오름차순 정렬

for i in edges:
    cost,a,b = i

    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        answer+=cost

print(answer)