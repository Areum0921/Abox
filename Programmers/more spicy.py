import heapq
def solution(scoville, K):
    answer = 0
    scoville=sorted(scoville)
    heap=[]
    [heapq.heappush(heap, i) for i in scoville]
    while(1):
        number=heapq.heappop(heap)+heapq.heappop(heap)*2
        heapq.heappush(heap,number)
        print(heap, len(heap))
        answer+=1
        if(heap[0]>K or len(heap)==1):
            break

    #print(answer)
    return answer

scoville = [1,2,3]
K = 88

solution(scoville,K)