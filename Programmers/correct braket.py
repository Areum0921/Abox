def solution(s):
    answer = True
    stack = []
    for i in s:
        if (i == '('):
            stack.append(i)
        else:
            if (stack):
                stack.pop()
            else:
                return False  # 짝이 안맞을때
    if (stack):  # 스택에 남아 있는게 있을때
        return False

    return True