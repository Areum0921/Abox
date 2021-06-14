def solution(N):
    i = 1
    answer = 0

    while i ** 2 <= N:  # 한 숫자로 나눠지면 나눈 수, 몫 쌍
        if i ** 2 == N:  # 1인 경우는 자기자신으로 나뉠때 factor가 1뿐이다.
            answer += 1

        elif N % i == 0:  # i로 나눠진다는뜻은 나눈 몫, i값이 factor
            answer += 2

        i += 1
    print(answer)
    return answer

N=2

solution(N)