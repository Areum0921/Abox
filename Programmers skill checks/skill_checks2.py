def solution(a, b):
    answer = 0
    am=max(a,b)
    bm=min(a,b)
    for i in range(bm, am + 1):
        answer += i
    print(answer)
    return answer

solution(5,3)