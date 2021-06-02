def find_team(team,a): # 소속 팀 찾기
    if team[a]!=a:
        return find_team(team,team[a])
    return a

def union_team(team,a,b): # 팀 합치기
    a=find_team(team,a)
    b=find_team(team,b)

    if a>b:
        team[a]=b
    else:
        team[b]=a

N,M=map(int,input().split(" "))

team = [i for i in range(N+1)]

for i in range(M):
    a,b,c = map(int,input().split(" "))

    if a==0: # 팀 합치기
        union_team(team,b,c)
    elif a==1: # 같은 팀인지 확인하기 (싸이클 여부)
        if find_team(team,b)==find_team(team,c):
            print('YES')
        else:
            print('NO')


