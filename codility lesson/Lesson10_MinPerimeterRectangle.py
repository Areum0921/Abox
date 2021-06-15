def solution(N):
    i = 1
    answer = []
    result=99999999999

    while i ** 2 <= N:
        if i ** 2 == N:  # i x i
            answer.append([i,i])

        elif N % i == 0:
            answer.append([i,N//i])

        i += 1

    for i in answer:
        result=min(result,2*(i[0]+i[1]))

    return result

N=36
print(solution(N))