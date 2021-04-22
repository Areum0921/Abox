def check(p): # 올바른 괄호인지 확인
    stack=[]
    for i in p:
        if(i=='('): # (일때는 집어넣고
            stack.append(i)
        else: # )일때는 뺀다. 뺄게없으면 올바른 괄호가 아님 즉 (가 있어야 )도가능
            if not stack:
                return False
            stack.pop()
    return True

def divide(p): # u,v로 나누기
    cnt=[0,0]
    for i in p:
        if(i=="("):
            cnt[0]+=1
        else:
            cnt[1]+=1
        if(cnt[0]==cnt[1]):
            u=p[:cnt[0]+cnt[1]]
            break
    v=p[cnt[0]+cnt[1]:]
    return u,v

def converse(p): # 괄호 뒤집기
    new_str=""
    for i in p:
        if(i=="("):
            new_str+=")"
        else:
            new_str+="("
    return new_str

def solution(p):
    answer = ''
    while(len(p)!=0):
        a,b = divide(p)
        if(check(a)): # u가 올바른거면 답에 추가
            #print("??", p, a, b)
            p=b # p변경
            answer+=a
        else:
            answer+='('+solution(b)+')'+converse(a[1:-1])
            break

    return answer

p="()))((()"
solution(p)
