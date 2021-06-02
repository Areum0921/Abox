# 서로소 집합을 활용한 사이클 판별
# 1. 루트노트가 서로 다를때 두 노드에 대해 union 연산
# 2. 루트노드가 서로 같다면 cycle 발생
# 3. 그래프에 포함되어있는 모든 간선에 대해 1,2번 과정 반복

def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a

v,e = map(int,input().split(" "))
parent = [i for i in range(v+1)] # 자기 자신을 부모로
print(parent)
cycle = False # 사이클 발생 여부

for i in range(e):
    a,b = map(int,input().split(" "))

    if find_parent(parent,a)==find_parent(parent,b): # 사이클이 하나라도 발생하면
        cycle=True
        break
    else:
        union_parent(parent,a,b)

print(cycle)



