def find_balanced(p): # 균형잡인 괄호 문자 자르기
    cnt = 0
    for i in range(len(p)):
        if p[i]== '(':
            cnt+=1
        else:
            cnt-=1
        if cnt == 0:
            return i # 인덱스 i 까지 균형잡힘.

def check(p): # 올바른 괄호문자인지
    stack=[]
    for i in p:
        if i=='(':
            stack.append('(')
        elif i==')':
            if len(stack)>0:
                stack.pop()
            else:
                return False
    return True

def solution(p):
    answer = ""
    if p == "":
        return answer

    idx = find_balanced(p)
    u = p[:idx+1]
    v = p[idx+1:]
    if check(u):
        answer=u+solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i]=='(':
                u[i]=')'
            else:
                u[i]='('
        answer += ''.join(u)
    return answer



p="))(("

print(solution(p))
