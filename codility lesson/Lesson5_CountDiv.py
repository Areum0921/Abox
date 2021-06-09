def solution(A, B, K):
    answer = B // K - A // K  # A%K==0이면 A가 1번더 빼짐
    # 6,12,2일때
    # 2,4,6
    # 2,4,6,8,10,12
    # 6-3 = 8,10,12
    # 6인경우 +1
    # 6,8,10,12
    if A % K == 0:
        answer += 1

    return answer

A=1
B=1
K=11
solution(A,B,K)