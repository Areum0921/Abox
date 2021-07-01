from collections import deque
n, l, r = map(int,input().split(" "))

national = [] # 국가별 인구수 저장

for i in range(n):
    population = list(map(int, input().split(" ")))
    national.append(population)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def make_union(x,y,idx):
    united = [] # 현재 연합국 좌표 저장
    united.append((x,y))

    q = deque()
    q.append((x,y))

    union[x][y]=idx # x,y에 해당하는 나라가 속한 연합 번호
    cnt = 1
    total_pop = national[x][y] # 인구 저장

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1 and l<=abs(national[x][y]-national[nx][ny])<=r:
                # 인접한 좌표면서, 아직 어느 연합에도 소속되어있지않고, 현재 국가와 인구 차이가 l~r명인 국가 
                q.append((nx,ny))
                cnt+=1 # 연합에 속한 국가 수
                union[nx][ny] = idx # nx,ny에 위치한 국가의 소속 연합 번호
                total_pop += national[nx][ny] # 연합군의 인구수 
                united.append((nx,ny)) # 연합군 좌표

    for i,j in united: # 연합군들의 좌표를 이용해, 해당 국가들의 인구 이동후 인구 수로 갱신
        national[i][j] = total_pop // cnt

    return cnt

answer = 0

while True:
    union = [[-1]*n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1:
                make_union(i,j,idx)
                idx+=1

    if idx == n*n: # 연합의 개수가 국가의 개수와 같으면 더이상 인구이동 불가. 탐색 끝
        break
    answer+=1

print(answer)

