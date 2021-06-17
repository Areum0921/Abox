# fibo결과값을 % 해주지 않으면 시간초과
def solution(A, B):
    answer = []

    fibo = [0] * 50002  # 1~50000개면 50001인데, 0부터시작이라
    fibo[0] = 0
    fibo[1] = 1

    for i in range(2, len(fibo)):
        fibo[i] = (fibo[i - 2] + fibo[i - 1]) % (2 ** 30)
    # % 2**30 : 숫자가 한없이 커지기 때문에 최대 값으로 mod 해서 저장한다.
    # 같은 연산이라도 숫자가 크면 시간이 더 많이 걸림.
    # 2**30은 B의 범위가 1~30으로 2^1 ~ 2^30 이다.
    # 큰 숫자 N이 있고, a,b가있을때 (a > b,이고 a는 b의 배수면)
    # N % a % b == N % b
    # 즉, 이 문제에서는 모듈러값이 2**1 ~ 2**30이므로 2**30은 모든 모듈러값의 배수가 될 수 밖에없다.
    # 또한, a > b 조건을 항상 만족하기위해 2**30
    for i in range(len(A)):
        answer.append(fibo[A[i] + 1] % (2 ** B[i]))
    print(answer)

    return answer

A=[50000,49999]
B=[20,15]
solution(A,B)