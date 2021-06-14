def solution(A):
    answer=[A[0]]
    for i in range(1,len(A)):
        answer.append(max(answer[i-1]+A[i],A[i]))

    return max(answer)

A=[3,2,-6,4,0]
solution(A)