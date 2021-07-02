def solution(N, stages):
    stages.sort()

    answer=[]
    rate = {}
    for i in range(1,N+1): # 1~N단계
        rate[i]=0

        passer = 0
        failer = 0
        for j in range(len(stages)):
            if stages[j]>i:
                passer+=1
            elif stages[j]==i:
                failer+=1
        if failer!=0: # 실패자가 1명이라도 있으면 실패율 계산
            # 실패자가 0명이면 실패율은 없음.
            rate[i]=failer/(failer+passer)


    rate = sorted(rate.items(), key=lambda x:x[1],reverse=True)
    for i in rate:
        answer.append(i[0])
    return answer

N=4
stages=[4,4,4,4]
solution(N,stages)