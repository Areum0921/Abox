# 2개의 최소비용 신장트리를 만들려면 1개의 신장트리를 만들고, 비용이 가장큰 경로를 차단하면 된다.

def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a > b:
        parent[a]=b
    else:
        parent[b]=a

v,e = map(int,input().split(" "))

parent = [i for i in range(v+1)]

edges=[]
last_cost=0 # 마지막 비용 저장용
result=0

for i in range(e):
    a,b,c=map(int,input().split(" "))
    edges.append((c,a,b))

edges.sort() # 비용 오름 차순 정렬
print(edges)
for i in edges:
    cost,a,b = i

    if find_parent(parent,a)!=find_parent(parent,b): # 싸이클이 발생하지않을때
        union_parent(parent,a,b)
        result+=cost
        last_cost=cost

print(result-last_cost)
