# 여행계획지가 같은 집합이면 yes
# 같은 집합은 서로 연결된 노드 집단

def find_parent(parent,x): # 특정 원소가 속한 집합
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,a,b): # 두 원소가 속한 집합 합치기
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b: # 숫자가 낮을수록 더 조상
        # 2의 부모노드가 1이고  3의 부모노드가 4면
        # 3을 부모노드 1 밑으로 합치기
        parent[b]=a
    else:
        parent[a]=b
N,M = map(int,input().split(" "))
parent =[0]*(N+1) # 부모노드 테이블
for i in range(N+1):
    parent[i]=i # 자기 자신을 부모로 초기화


for i in range(N): # 루트 개수는 N개
    route = list(map(int,input().split()))
    for j in range(N):
        # 여행지 번호는 1번부터 시작
        if route[j]==1: # i -> j로 연결된경우 합치기
            union_parent(parent,i+1,j+1)

plan = list(map(int,input().split())) # 계획세우고
# 계획의 여행지들의 부모노드가 모두 같으면 YES
check=parent[plan[0]] # 첫번째 여행지의 부모
answer=True
for i in plan:
    if parent[i]!=check:
        answer=False
        break
if answer==False:
    print('NO')
else:
    print('YES')

