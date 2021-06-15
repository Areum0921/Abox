# n개의 플래그 -> 거리 n개 이하

def solution(A):
    N = len(A)
    peaks = [False] * N # 피크 인덱스 체크용
    for i in range(1, len(A) - 1):
       if A[i] > max(A[i-1],A[i+1]):
           peaks[i]=True # 피크 지점 체크


    next_peaks=[0] * N  # 해당 인덱스 기준으로 가장 가까운 peaks 위치
    next_peaks[N-1] = -1 # 마지막은 peak 될수 없음

    for i in range(N-2,-1,-1):
        if peaks[i]:
            next_peaks[i]=i
        else:
            next_peaks[i]=next_peaks[i+1]

    print(next_peaks)

    i=1
    result=0
    # 깃발을 꼽는 모든 개수 경우에 대해서 계산.
    while (i-1)*i <= N: # N 안에서 꽂을 수 있는 깃발의 최대 개수, N=10이면, 최대 3개, (3-1)*3 = 6 < 10
                        # 4개를 꽂으려면 간격때문에 불가능 (4-1)*4 = 12 < 10 x
                        # i-1 <- 간격 거리 , i = 깃발 수 라고 생각하면 된다.
                        # 깃발을 3개꼽으려면 1간격당 3거리, 간격은 2개 = 간격 수 2 x 최소 필요 거리 3 = 6
        pos=0 # position
        num=0 # flag num

        while pos < N and num < i:
            print(i, pos, num)
            pos = next_peaks[pos] #
            if pos == -1:
                break
            print(i, pos, num)
            num += 1
            pos += i

        print("=============",num)
        result = max(result,num)
        i+=1

    return result



"""
40%
def solution(A):
    answer=[]
    ans=0
    for i in range(1,len(A)-1):
        if A[i]>max(A[i-1],A[i+1]):
            answer.append(i) # 피크 위치
            
    if len(answer) == 0: # 피크 0개
        return 0
    
    if len(answer) == 1: # 피크 1개
        return 1
    

    dis=len(answer)
    i,j=0,1
    ans=1
    # 첫번째 깃발을 기준으로 시작해 제한 거리를 하나씩 줄여가며 최대한 다음 깃발에 꼽기

    while j!=len(answer): # 꼽을 수 있는대로 꼽기

        flag1 = answer[i] # 기준 지점
        flag2 = answer[j] # 다음 지점

        if flag2-flag1 < dis: # 일정 거리 미만이면 flag2 삭제, 다음 peak로 이동
            dis-=1 # 제한거리 1 감소
            j+=1 # 다음 플래그와 비교
        else: # 깃발 간격이 조건에 충족되면
            ans+=1
            i=j # 기준지점 갱신
            j+=1 # 다음 깃발로

    print(ans,dis)

    return ans
"""
A=[1,5,3,4,3,4,1,2,3,4,6,2]
print(solution(A))
