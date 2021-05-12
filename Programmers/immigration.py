# 걸리는 시간이 되는 범위를 잡는다.

def solution(n, times):
    answer = 0
    max_time=max(times) * n # 가장 길게 걸리는 심사관한테 모두 줄섰을때 걸리는 시간
    # 시간을 점점 줄여가면서 계산
    min_time=1

    while min_time<=max_time: # 같아지면 멈춤
        mid_time = (min_time+max_time)//2 # 심사관 1명당 주어진 심사 시간
        pass_people=0
        print(min_time,max_time,mid_time)

        for i in times:
            pass_people += mid_time//i # i초 걸리는 심사관이 주어진 시간동안 보낼 수 있는 사람 수
            if pass_people >= n : # 해당 시간안에 심사관들이 n명을 보낼 수 있으면
                answer=mid_time # answer에 현재 mid_time 저장
                max_time = mid_time-1 # max_time를 줄여나가며 while이 멈출때까지 다시 반복
                break

        if pass_people < n: # n명을 보낼 수 없을때 min_time에 1초씩 늘려도 상관없지만
            # 현재 mid_time에도 n명을 보낼수 없으므로, 최소값을 mid_time+1로 늘려도된다.
            min_time = mid_time + 1

    print(answer)
    return answer
n=6
times=[7,10]
solution(n,times)