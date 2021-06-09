def solution(A):
    answer = 0
    count_one=A.count(1) # 1의 개수가 중요
    # 0을 만날때마다 0 인덱스 이후의 1의 개수를 더해주면된다.

    for i in range(len(A)):
        if A[i]==0:
            answer+=count_one
        if A[i]==1:
            count_one-=1
        if answer > 1000000000: # 조건 처리 
            return -1

    return answer

A=[0,1,0,1,1]
solution(A)