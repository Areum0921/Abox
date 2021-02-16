def solution(n, m):
    answer = []
    n2=n
    m2=m
    while(1): #최대 공약수
        gcd=m2%n2
        if(gcd!=0):
            m2=n2
            n2=gcd
        elif(gcd==0):
            break
    answer.append(n2)
    answer.append(n*m/n2)#최소공배수
    return answer