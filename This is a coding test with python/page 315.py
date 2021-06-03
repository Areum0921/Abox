N,M=map(int,input().split())
ball=list(map(int,input().split()))
answer=0
"""
for i in range(len(ball)):
    for j in range(i+1,len(ball)): # i+1번째 공부터 검사.
        if ball[i]!=ball[j]: # 공의 무게가 다를때
            print(ball[i],ball[j])
            answer+=1
"""
# for문 1번 사용하는 경우

weight=[0]*11 # 무게 1~10까지인 볼링공 개수 저장
# 현재 공과 다른 무게의 공들을 집을 수 있음. (같은 무게여도 다른 볼로 취급)

for i in ball:
    weight[i]+=1


for i in range(1,len(weight)):
    N-=weight[i] # 무게 i인 볼과 조합 가능한 다른 무게의 볼 개수
    # N을 계속 빼는 식으로 계산하는 이유
    # 볼의 무게가 1,1,5,4,3 일경우
    # 무게가 1인볼을 집었을때 5,4,3 3가지를 고를 수 있다.
    # 무게가 1인볼은 2개이고, 서로 다른 볼로 간주하여 2 x (5-2) = 6가지다.
    # 다음으로 무게가 5인 볼을 집었을때 1,4,3 3가지를 고를 수 있다.
    # 하지만 1을 고르는 경우는 이전에 첫번째로 1을 고르는 경우에 계산 되었으므로 중복된다.
    # 즉, 1을 제외하고 남은 볼 3개에서 무게가 5인 볼의 개수를 빼 계산한다.
    # 1 * (3-1) = 2개
    # 1 * (2-1) = 1개
    # (1,5) (1,4) (1,3) (1,5) (1,4) (1,3) // (5,4) (5,3) // (4,3) = 총 6+2+1개
    answer+=weight[i]*N


print(weight)
print(answer)