from collections import deque

def bfs(x,computers,check):
    q = deque()
    q.append(x)

    while (q):
        num1 = q.popleft()
        check[num1]=True # num1번 컴퓨터 방문처리
        for i in range(len(computers)):
            if(computers[num1][i]==1 and check[i]==False): # i번컴퓨터 방문안했고, num1번 컴퓨터와 연결되어있으면
                q.append(i)

def solution(n, computers):
    answer=0
    check = [False] * len(computers)
    for i in range(len(computers)):
        if(check[i]==False):
            answer+=1
            bfs(i,computers,check)

    print(answer)
    return answer

computers=[[0, 1, 0], [1, 0, 1], [0, 1, 0]]
n=3
solution(n,computers)