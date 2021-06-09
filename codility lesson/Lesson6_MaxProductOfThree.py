# 내림차순, 음수의 경우 2개 곱하면 양수.
# 제일 작은 음수 2개*제일큰 양수 와 큰 양수 3개 곱 비교

def solution(A):
    A.sort(reverse=True)

    answer = max(A[0]*A[1]*A[2],A[0]*A[-1]*A[-2])

    return answer


A=[-7,-5,3,6,4]
solution(A)