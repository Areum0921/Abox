# 중간 시간을 기점으로 시간을 늘렸다, 줄였다 하면서 최적의 시간을 찾는다.

def solution(n, times):

    max_time = max(times) * n # 제일 오래 걸리는 심사위원이 모두 심사했을때
    min_time = 1 # 1~max_time을 탐색해 가장 빠른 시간 검색 min(times)*n은 최소시간이 아니다. 여러명이 함께 심사하기 때문에

    while min_time<=max_time:
        mid_time = (max_time+min_time)//2 # 중간시간부터 탐색
        passer = 0 # 통과한 사람 수

        for i in times:
            passer += mid_time//i # mid_time안에 각 심사관이 통과시킬 수 있는 사람 수
            if passer>=n: # 통과 시킬 수 있는 사람수가 n이상이면 시간을 줄여본다 (제일짧은시간안에 n명을 보내는게 목표)
                answer = mid_time # 일단 이 시간안에는 n명 만큼 통과시킬수 있음
                max_time = mid_time-1 # 시간을 줄여서 탐색해보자.
                break
        if passer < n : # 통과 시킬 수 있는 사람수가 n보다 작으면 시간을 늘려본다(n명은 통과시켜야 하므로)
            min_time = mid_time+1

    return answer



n=6
times=[7,10]
solution(n,times)