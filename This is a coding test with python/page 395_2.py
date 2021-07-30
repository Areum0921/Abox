def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,x,y):
    a = find_parent(parent,x)
    b = find_parent(parent,y)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a

G = int(input())
P = int(input())

parent=[0]*(G+1)
answer = 0

for i in range(G+1):
    parent[i]=i

# i번 비행기는 각각 1 ~ g(i)번탑승구에 도킹가능.
# 각 탑승구의 부모노드를 찾아, 부모노드가 0이 아니면 도킹 가능.
# 연결가능한 가장 뒷 번호의 탑승구에 도킹.
# 해당 탑승구의 맨위 조상이 맨앞 번호 탑승구가 아니면 1~마지막 탑승구 사이 중간에 비어있는 탑승구가 존재함을 뜻.
for i in range(P):
    root = find_parent(parent,int(input()))
    if root==0:
        break
    else:
        union_parent(parent,root,root-1)
        answer +=1
    print(parent)

print(answer)