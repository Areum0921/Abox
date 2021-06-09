# O(N+M)
def solution(S,P,Q):

    answer=[]
    for i in range(len(P)):
        part=S[P[i]:Q[i]+1]

        if 'A' in part:
            answer.append(1)
        elif 'C' in part:
            answer.append(2)
        elif 'G' in part:
            answer.append(3)
        else:
            answer.append(4)

    return answer

S='CAGCCTA'
P=[2,5,0]
Q=[4,5,6]
solution(S,P,Q)