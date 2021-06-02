# 최소비용 신장트리
# 1. 간선 데이터를 비용 기준으로 오름차순 정렬
# 2. 간선을 하나씩 확인하며 현재 간선이 사이클을 발생시키는지 확인
# 2-1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
# 2-2. 사이클이 발생하는 경우 포함하지 않음
# 3. 모든 간선에 대해 2번 과정 반복


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

v, e = map(int,input().split(" "))
parent = [i for i in range(v+1)]

edges=[] # 간선 정보 담을 리스트
result=0 # 비용

for _ in range(e): # 간선에 대한 비용
    a,b,cost = map(int,input().split(" "))
    edges.append([cost,a,b])

edges.sort() # 간선 비용 기준으로 오름차순

for i in edges: # 비용이 적은 경로 부터 확인
    cost, a, b = i
    print(cost,a,b)
    # 사이클이 발생하지 않을때 해당 간선 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b) # 사이클이 발생하지 않음 -> 합치기
        result+=cost

print(result)