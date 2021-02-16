def solution(dartResult):
    answer = []
    t=''
    for i in dartResult:
        if i.isnumeric():#10 == "1"+"0"
            t += i
        elif i == 'S':
            answer.append(int(t))
            t = ''
        elif i == 'D':
            answer.append(int(t) ** 2)
            t = ''
        elif i == 'T':
            answer.append(int(t) ** 3)
            t = ''
        elif i == '*':
            if(len(answer)>1):#직전에 더한 숫자가 있을때
                answer[-2]*=2
            answer[-1]*=2
        elif i == '#':
            answer[-1]*=-1


    print(sum(answer))
    return sum(answer)


dartResult='1T2D3D#'
solution(dartResult)