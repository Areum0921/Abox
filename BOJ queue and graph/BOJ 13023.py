# 꼬리물기식 친구, i는 i+1과 친구, i+1은 i+2와 친구인 관계, 해서 4다리까지 존재하는지 살펴보기.
# 최소 i~i+4에서 꼬리물기 친구관계 필요.
import sys
N,M=map(int, sys.stdin.readline().split(" "))
friend=[[]*N for i in range(N)]
visit = [False] * N

#print(friend)
for j in range(M): # 인접 리스트.
    a,b = map(int, sys.stdin.readline().rstrip().split(" "))
    friend[a].append(b)
    friend[b].append(a)
#print(friend)


def find(n,dep):
    global answer
    if answer==True: # 이미 존재함을 발견했으면 추가 검색x
        return
    if dep==4: # 연결된 관계가 4개이상 존재.
        answer = True
        return

    for i in friend[n]: # n과 친구관계인 애들 찾기
        if(visit[i]==False): # 체크안했을경우
            visit[i]=True # 체크해주고
            find(i,dep+1) # 해당 친구 기준으로 또 연결된 친구 찾기
            visit[i]=False # 연결된 친구가 없으면 뒤로가서 다른친구로 다시시작

answer=False
for i in range(N):
    visit[i] = True
    find(i,0)
    visit[i] = False

#print(answer)
if(answer):
    print(1)
else:
    print(0)