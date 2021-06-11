# 그려보는게 이해하는데 도움된다.

def solution(H):
    stack=[]
    cnt=0

    for i in H:
        while len(stack)>0 and stack[-1]>i: # 최근 벽돌보다 낮은 벽돌을 넣을때
            # 스택에 값이 있고, 지금 넣는 벽돌의 높이 이하 벽돌이 나올때까지
            # 최근에 넣은 순으로 벽돌 제외
            stack.pop()

        if len(stack)==0 or stack[-1]<i:
            # 위에서 제외하다보면 stack이 비거나, 마지막 벽돌보다 i 높이가 더 높다.
            stack.append(i)
            cnt+=1

    return cnt



H=[3,1,4,5,2]
solution(H)