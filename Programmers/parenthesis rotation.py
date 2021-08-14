# 스택만 구현하면 간단하게 풀림.
def check(s):
    stack = []
    for i in s:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
        else:
            if i==')' and '(' in stack:
                stack.pop()
            elif i=='}' and '{' in stack:
                stack.pop()
            elif i==']' and '[' in stack:
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False

def solution(s):
    answer = 0

    for i in range(len(s)):
        rotate_s = s[i:]+s[:i] # s를 왼쪽으로 한칸씩.
        if check(rotate_s)==True:
            answer+=1

    return answer

s="["
solution(s)