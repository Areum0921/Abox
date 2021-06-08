# for문에서 sum(A[i:]) 쓰면 O(N*N)으로 시간초과
def solution(A):
    answer = 9999999
    first=0 # 앞부분
    end=sum(A) # 뒷부분
    for i in range(len(A)-1):
        first+=A[i]
        end-=A[i]
        gap=abs(first-end)
        if gap<answer:
            answer=gap

    return answer

A=[3,1,2,4,3]
solution(A)