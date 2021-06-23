from itertools import combinations

def cal_range(select,house):
    result=0
    for x,y in house:
        temp = int(1e9)
        for cx,cy in select: # 존재하는 치킨집중 가장 가까운 거리 찾기.
            temp = min(temp,abs(x-cx)+abs(y-cy))
        result += temp # 지금 집에서 가장 가까운 치킨 거리 더하기.

    return result

def solution(N,M,board):

    answer=0
    house=[] # 집 위치
    chicken=[] # 치킨집 위치

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==1:
                house.append([i,j])
            elif board[i][j]==2:
                chicken.append([i,j])

    select = list(combinations(chicken,M)) # 전체 치킨집 중에서 M개 고르는 경우의 수들(치킨집 인덱스)

    answer=int(1e9)
    for i in select: # 가능한 치킨집 조합중에서 가장 작은 치킨거리 합 찾기.
        answer=min(answer,cal_range(i,house))

    print(answer)


N=5
M=2
board=[[0,2,0,1,0],[1,0,1,0,0],[0,0,0,0,0],[2,0,0,1,1],[2,2,0,1,2]]
solution(N,M,board)