# O(N)
def solution(S):
    stack = []

    for i in S:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            if len(stack)>0:# 쌓인 스택이 있다면 확인
                x = stack.pop() # 최근에 열린 괄호부터 닫혀야 함.
                if x == '(' and i == ')':
                    continue
                elif x == '{' and i == '}':
                    continue
                elif x == '[' and i == ']':
                    continue
                else:
                    return 0
            else: # 쌓인 스택이 없다면 불완전 괄호쌍
                return 0

    if len(stack) > 0: # 완전한 괄호쌍이려면 stack에 남은게 없어야 한다.
        return 0
    else:
        return 1


S="{[()()}"
print(solution(S))