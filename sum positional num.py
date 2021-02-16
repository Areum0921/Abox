def solution(n):
    answer = 0
    string=str(n)
    for i in range(len(string)):
        answer+=int(string[i])

    return answer

n=123
solution(n)