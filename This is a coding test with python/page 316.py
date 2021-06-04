import heapq

def solution(food_times, k):

    if sum(food_times)<=k:
        #print(-1)
        return -1

    q=[] # 시간이 작은 음식부터

    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1)) # 시간, 음식번호
    # q의 길이가 현재 음식 개수
    q.sort() # 시간이 짧은 순으로 정렬

    length=len(food_times) # 남은 음식 개수
    prev=0 # 이전 음식시간 (제일 짧은 음식이 2초걸리는데, n바퀴 돌면 다른 음식들도 n*2초가 줄음)
    eat=0 # 총 음식 먹은 시간, k과 비교
    while eat + ((q[0][0]-prev) * length) <=k:
        now = heapq.heappop(q)[0] # 지금 먹은 음식의 시간
        eat += (now-prev) * length
        prev = now
        length -= 1 # 다먹었으니, 남은 음식 개수 줄이기
    print(q)
    k-=eat # 남은 시간 (1바퀴는 다 못먹고 순서대로(음식번호순) 먹으면 된다.)
    answer = sorted(q, key=lambda x : x[1]) # 기존 시간순 정렬에서 음식 번호순으로 다시 정렬
    # 이때 .sort()는 저장되는것과 달리 sorted 정렬을 사용하려면 변수에 저장해야 한다.
    # a = 3,5,2
    # a.sort() = 2,3,5 유지
    # sorted(a) = 이때만 2,3,5
    # a 다시부르면 3,5,2
    print(answer)
    #print(q[k%length][1])
    return answer[k%length][1] # 음식 번호순으로 정렬후 k번째에 해당하는 음식번호 반환

food_times=[1,5,4]
k=5
solution(food_times,k)