def solution(n):
    answer = 0
    arry = [True] * (n+1)
    arry[0] = False
    arry[1] = False

    sqr = int(n ** 0.5)

    for i in range(2, sqr + 1):

        if arry[i] == True:
            for j in range(i+i, n+1, i):

                arry[j] = False
    answer=arry.count(True)
    print(answer)
    return answer

solution(5)