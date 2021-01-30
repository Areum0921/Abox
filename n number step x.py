def solution(x, n):
    answer = []
    answer.append(x)
    if(x!=0):
        for i in range(x+x, n*x+x, x):
            answer.append(i)
    else:
        answer=[0] * n

    print(answer)
    return answer

x=0
n=6
solution(x,n)