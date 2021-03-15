# combination 사용하기
# 먼저 사람수를 반으로 나눠 팀을 이룰 수 있는 구성 만들기 (각 팀의 인원수는 달라도되고, 1명이상)
from itertools import combinations
N=int(input())
S = [list(map(int,input().split(" "))) for _ in range(N)]
all_member=[i for i in range(N)]
make_team=[]
stat_gap=10000

for i in range(1,N): #각팀의 멤버 수는 1명이상, 최대 N-1명까지
    for team in list(combinations(all_member,i)):
            make_team.append(team)
print(make_team)

# N까지 숫자를 이용해 N의 절반씩 모든 조합 구하기, 같은 원소구성은 중복으로 취급
# make_team[i] 와 make_team[-i-1] 이 합쳐지면 all_member와 동일
for i in range(len(make_team)//2):
    team=make_team[i]
    stat_1=0 # 첫번째팀 능력치 합
    for j in team:
        for k in team:
            if(j!=k):
                stat_1+=S[j][k]

    team=make_team[-i-1]
    stat_2 = 0  # 두번째팀 능력치 합
    for j in team:
        for k in team:
            if (j != k):
                stat_2 += S[j][k]
    if(abs(stat_1-stat_2)<stat_gap):
        stat_gap=abs(stat_1-stat_2)

print(stat_gap)
