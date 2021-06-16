
def solution(N,P,Q):
    answer = [0] * len(P)

    # 소수 구하기
    prime = []
    num = [False] * (N + 1)

    # N이 최대 숫자 범위니까 제일작은 소수인 2와 곱하면 N//2까지만 구해도 N을 만들 수 있다.
    for i in range(2, N // 2 + 1):
        if num[i] == False:
            prime.append(i)
            for j in range(i + i, N + 1, i):
                num[j] = True

    print(prime)
    semi_prime = [False] * (N+1) # semi_prime 여부

    for i in range(len(prime)):
        for j in range(len(prime)):
            d = prime[i] * prime[j]
            if d <= N: # N까지만 구하면 된다.
                semi_prime[d] = True
            else:
                break


    count_semi = [0]*(N+1) # 각 인덱스까지 누적 semi_prime이 몇개인지
    for i in range(1,len(semi_prime)):
        if semi_prime[i]:
            count_semi[i]=count_semi[i-1]+1
        else:
            count_semi[i]=count_semi[i-1]

    for i in range(len(P)):
        # 6~10일때 앞부분인 6이 semiprime인데 이 경우 2번 빼지는걸 방지하기 위해 6-1의 누적 카운트로 계산
        # 6 -> 4,6 - 2개
        # 10 - > 4,6,9,10 - 4개
        # 총 3개
        answer[i] = count_semi[Q[i]] - count_semi[P[i]-1]

    print(answer)
    return answer
P=[1,3,6,5,9]
Q=[10,15,23,22,23]
N=26
solution(N,P,Q)
