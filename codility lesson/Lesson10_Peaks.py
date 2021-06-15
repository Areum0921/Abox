# 각 부분에서 피크를 따지는게 아니라
# 처음 A에서 피크를 따진후, 자른뒤 피크 유무 확인
def solution(A):
    N=len(A)

    if N < 3 : return 0

    peaks=[]

    for i in range(1,len(A)-1):
        if A[i] > max(A[i-1],A[i+1]):
            peaks.append(i) # 피크지점 인덱스


    num=len(peaks) # 피크 개수

    if num == 0: # 피크 자체가 없는경우
        return 0
    if num == 1:
        return 1

    # 피크 지점 인덱스가 블록 범위 안에 있는지 확인

    for i in range(num,0,-1): # 최대 블록개수는 피크 수
        # 가능한 최대 블록수부터 하나씩 줄여 탐색
        if N % i == 0:
            cnt = 0
            ele = N // i # 1블록당 원소 수
            block= [0] * i # peak 배치한 블록수
            # 각 블록안에 peak가 모두 포함되면 block의 모든 요소값은 1
            for j in range(num):
                idx = peaks[j] // ele # 원소 개수로 나눠 peaks[j]에 해당하는 인덱스가 
                # 몇번째 블록에 있는지 idx로 저장
                # peak가 인덱스 3에 있는데, 각 블록마다 4개의 요소를 가지면
                # 3 // 4 = 0으로 0번째 블록에 해당한다
                # peak가 인덱스 7에 있으면 7//4 = 1 , 1번째 블록에 해당한다.
                if block[idx] == 0:
                    block[idx]=1
                    cnt+=1

            if cnt==i: # i(목표 블록수)와 실제 블록수 cnt가 같으면 조건에 맞음
                return i

    return 1

A=[1,2,3,4,3,4,1,2,3,4,6,2]
print(solution(A))
