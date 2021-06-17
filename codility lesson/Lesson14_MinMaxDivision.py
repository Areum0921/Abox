# 주어진 배열을 K개의 블록으로 나눠 각 블록의 합 최대치가 가장 낮을때 합 리턴

# 몇개의 블록이 생기는지
def check(A,c,s): # A, max block cnt, max block size
    temp_sum = 0
    temp_cnt = 0 # 새로 생성된 블록 수

    for ele in A: # A의 각 요소 ele
        if temp_sum + ele > s: # 원소 합이 mid값을 넘으면 다음 블록에서 계산
            temp_sum = ele
            temp_cnt += 1 # 블록 생성하기, 생성한 블록수 카운트
        else:
            temp_sum += ele
        if temp_cnt >= c: # temp_cnt >= c에 =가 붙는이유는
            # 위에서 block 1개 생성될때마다 temp_cnt가 증가하는데
            # 블록 1개 생성시, 존재하는 블록은 2개
            # 블록 2개 생성시, 존재하는 블록은 3개이기 때문.

            return False

    return True



def solution(K,M,A):
    lower = max(A) # 결과로 나올 수 있는 최소값 , 1원소 == 1블록
    upper = sum(A) # 결과로 나올 수 있는 최대값 , 전체원소 == 1블록
    print(lower, upper)

    if K==1:
        return upper
    elif K>=len(A):
        return lower

    while lower <= upper:
        mid = (lower + upper) // 2 # 최소값+최대값의 중간지점
        # 각 블록의 합 제한을 mid로
        if check(A,K,mid): # k개만큼 블록을 만들 수 있으면
            upper = mid-1 # 합 제한을 낮춰서 다시 또 k개만큼 블록 만들어지는지 확인
        else: # 합 제한값이 mid일때 k개의 블록을 만들 수 없다면, 합 제한값을 높인다.
            # 만들 수 없는 경우는 1블록당 최대 값이 mid일때
            # k개보다 더 많은 블록이 필요할 때다.
            lower = mid+1
        print(lower,upper)
    print("result",lower)

A=[2,1,5,1,2,2,2]
solution(3,5,A)










K=3
M=5 # 배열 요소의 최대값
A=[2,1,5,1,2,2,2]