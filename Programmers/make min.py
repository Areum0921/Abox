def solution(A,B):
    answer = 0
    A=sorted(A)
    B=sorted(B,reverse=True)
    # 제일큰값이랑 제일작은값 곱해주기.
    for i in range(len(A)):
        answer+=A[i]*B[i]
    return answer