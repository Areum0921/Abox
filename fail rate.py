def solution(N, stages):
    answer = []
    fail_rate=[]
    high_stage=max(stages)

    for i in range(1,N+1):
        passer = 0 # 스테이지별 통과자
        failer = 0 # 현재 스테이지를 못깬사람
        for j in range(len(stages)):

            if(stages[j]>i): #현재 있는 스테이지가 i단계보다 높으면 통과자
                passer+=1
            elif(stages[j]==i):#현재 단계를 못벗어난 사람
                failer+=1

        print(passer+failer, failer)
        print("fail",len(fail_rate),N)
        if(passer==0 and len(fail_rate)<high_stage):
            print("11")
            fail_rate.append(1)
        elif(len(fail_rate)>=high_stage):
            print("222")
            fail_rate.append(0)
        else:
            print("333")
            fail_rate.append(failer/(passer+failer))

    print(fail_rate)
    for i in range(N):
        answer.append((fail_rate.index(max(fail_rate))+1))
        fail_rate[fail_rate.index(max(fail_rate))]=-1

    print(fail_rate, answer)
    return answer
#key를 이용해서 간단하게 구현해보기
N=6
stages=[4,4,4,4]
solution(N, stages)