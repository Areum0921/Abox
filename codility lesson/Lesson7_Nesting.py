def solution(S):
    stack=[]
    for i in S:
        if i=='(':
            stack.append(i)
        else:
            if len(stack)>0:
                stack.pop()
            else:
                return 0
    if len(stack)==0:
        return 1
    else:
        return 0
S='((((()))))'
print(solution(S))