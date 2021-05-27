# 기초 bfs 문제

from collections import deque

def bfs(case,x,y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q=deque()
    q.append([x,y])

    while q:
        a,b=q.popleft()
        for i in range(4):
            num1=a+dx[i]
            num2=b+dy[i]
            if 0<=num1<len(case) and 0<=num2<len(case[0]):
                if case[num1][num2] == 0:
                    q.append([num1,num2])
                    case[num1][num2] = 1


def solution(case):
    cnt=0
    for i in range(len(case)):
        for j in range(len(case[0])):
            if case[i][j]==0:
                print("??",i,j)
                bfs(case,i,j)
                cnt += 1
    print(cnt)

case=[[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
solution(case)