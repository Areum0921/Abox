def solution(jobs):
    # 빨리 끝나는거 부터 하면 평균시간 줄음
    answer = 0
    jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간이 작은대로 정렬
    #print(jobs)
    req = len(jobs)
    time = 0

    while (len(jobs) != 0): # 요청이 비워질때까지 반복
        for i in range(len(jobs)):
            if jobs[i][0] <= time:  # 시작하는 가능 시간이 현재시간보다 같거나 이전이면
                time += jobs[i][1]  # 현재 시간 + 작업시간
                answer += time - jobs[i][0]  # 작업이 끝난 시간 - 요청시간 = 대기 + 작업완료시간
                #print(jobs, answer, time)
                jobs.pop(i) # 현재 작업 삭제
                # pop(0)이 아닌이유 10,2 / 3,5 인경우 소요시간은 10,2가 적으나 3초때에 10,2 처리불가
                # 즉 이때 처리할수있는 요청을 처리하고, 해당요청 삭제
                break
            if i==len(jobs)-1: # 모든 요청을 확인했으나, 실행가능한 요청이 없을때
                time +=1
    print(answer//req)
    return answer//req

jobs=[[0, 20], [1, 9], [2, 6]]
solution(jobs)