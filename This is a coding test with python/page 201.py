# 중간길이 부터 잘라보고 모자르면 자르는 길이를 줄이고, 넘치면 자르는 길이를 늘려본다.

def solution(tteok,M):
    tteok=sorted(tteok)
    end = tteok[-1] # 가장 긴 떡의 길이
    start=0

    while start<=end:
        answer=0 # 떡을 길이 mid로 잘랐을때 잘라낸 떡의 길이 합
        mid = (start+end)//2

        for i in tteok:
            if i > mid:
                answer+=i-mid

        if answer < M: # 자른 떡의 양이 더 적으면
            end=mid-1
            
        else: # 자른 떡의 양이 넘치면
            answer=mid
            start=start+1

    print(answer)

tteok = [19,15,10,17]
M=6
solution(tteok,M)
