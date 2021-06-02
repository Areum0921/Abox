# 서로소 집합

def find_parent(parent,x): # 재귀로 루트 노드 찾기. 경로 압축 기법. 기존 find는 노드 v, 연산 m일때 O(vm) -> 비효율
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b): # 두 원소가 속한 집합 union
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b: # a의 루트노드보다 b의 루트노드가 더 크면 b의 루트노드는 a의 루트노드가된다.
        parent[b]=a
    else:
        parent[a]=b

v, e = map(int,input().split(" ")) # 노드개수, 간선(union)
parent=[0]*(v+1) # 부모 테이블

for i in range(1,v+1):
    parent[i]=i # 자기 자신으로 초기값

for i in range(e): # union 입력 및 수행
    a,b = map(int,input().split(" "))
    union_parent(parent,a,b)

print("각 원소가 속한 집합",end=" ")
for i in range(1,v+1):
    print(find_parent(parent,i),end=" ")
print()
print("부모 테이블",parent[1:])