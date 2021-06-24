# 문제가 원형으로 주어졌을 경우, 일직선으로 만드는 방법도 생각해보자.
from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist)+1
    weak_point = len(weak)  # 초기 weak 지점 개수

    for i in range(len(weak)): # 원형을 일직선으로 만들어준다.
        weak.append(weak[i] + n)

    for start in range(weak_point): # 각 지점에서 출발하는 모든 경우 (시작지점이 0번째 취약점~마지막 취약점)
        # 일직선으로 만든 리스트에서 초기 weak 지점 개수만큼을 커버 하면 된다.
        for fr in list(permutations(dist,len(dist))): # 친구들을 보내는 모든 경우의 수.
            cnt = 1 # 정찰친구 카운트
            pos = weak[start] + fr[cnt-1] # 시작지점부터 fr[인덱스]에 해당하는 친구가 가능한 거리
            for idx in range(start,start+weak_point): # 시작 취약점부터 마지막 취약점 까지 (개수) 초기 len(weak)
                if pos < weak[idx]: # 현재 친구가 남은 취약점을 못돌때
                    cnt+=1 # 친구 한명더 투입
                    if cnt > len(dist): # 친구 수는 초기 친구수를 초과할 수 없음.
                        break
                    pos = weak[idx]+fr[cnt-1] # 투입한 친구의 position 계산. 반복
            answer = min(answer,cnt)

    print(answer)
    if answer > len(dist): # 최소값이 기존 친구 수보다 크면 모두 방문 불가
        return -1
    return answer

n=200
weak=[0, 10, 50, 80, 120, 160]
dist=[1, 10, 5, 40, 30]
solution(n,weak,dist)