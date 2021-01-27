def solution(n):
    answer = []
    strn=str(n)
    for i in range(len(strn)-1,-1,-1):
        answer.append(int(strn[i]))

    return answer

n=12345
solution(n)
